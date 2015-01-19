#!/usr/bin/python2.7
from ftplib import FTP
import smtplib
import csv
import os
import mysql.connector
import shutil
from datetime import datetime
import time
from decimal import *

class ProcessSBCtoDB:
	def __init__(self, ftpIP, ftpUser, ftpPassword):
		self.ftpIP = ftpIP
		self.ftpUser = ftpUser
		self.ftpPassword = ftpPassword

		self.dbuser = 'root'
		self.dbhost = '172.16.3.65'
		self.database = 'Approved_Performance'
		self.dbpassword =  'PLOK1234plok'

		self.timenow = datetime.now()
		self.current_time = time.mktime(self.timenow.timetuple())
		self.filename = 'MATRACK.CSV'
		self.homedir = '/home/musher/Approved_Performance/Approved_Performance/Amazon/Backend'
		#self.homedir = '/home/Amazon/Amazon'

	def main_logic(self):
		#self.ftpgetcsv()
		self.import_csv_into_db()

	def ftpgetcsv(self):
		os.chdir(self.homedir)
		try:
			local_file = open('./CSVs/%s' %self.filename, 'wb')
		except:
			print "Unable to open file MATRACK.CSV for writing in function ftpgetcsv"
			return
		try:
			ftp = FTP('%s' % self.ftpIP, timeout=5)
			ftp.login(user='%s' % self.ftpUser, passwd='%s' % self.ftpPassword)
		except:
			Failed_message = "Unable to connect to FTP in function ftpgetcsv"
			print Failed_message
			self.send_email(Failed_message)
			exit(1)

		ftp.cwd("/sbc/invfeed/")
		if 'CSV_ARCHIVE' not in ftp.nlst():
			ftp.mkd('CSV_ARCHIVE')
		try:
			ftp.retrbinary('RETR ' + self.filename, local_file.write)
			local_file.close()
		except:
			print "File MATRACK.CSV is not present"
			return

		statinfo = os.stat('./CSVs/%s' %self.filename)

		if statinfo.st_size == 0:
			print "0 Byte file"
			os.remove('./CSVs/%s' %self.filename)
			ftp.close()
			exit(2)
		else:
			ftp.rename(self.filename, "./CSV_ARCHIVE/%s-%s" %(self.filename,self.current_time))
			ftp.close()

	def import_csv_into_db(self):

		os.chdir(self.homedir)
		try:
			csv_file = open('./CSVs/%s' %self.filename, 'rb')
		except:
			Failed_message = "Unable to open MATRACK.CSV in folder %s/CSVs" %(self.homedir)
			print Failed_message
			#self.send_email(Failed_message)
		#	exit(2)
		reader = csv.reader(csv_file)
		for row in reader:
			temp_columns = []
			for column in row:
				temp_columns.append(column)

			index = 0
			while index < len(temp_columns):
				if index == 4 or index == 5:
					temp_columns[index] = Decimal(temp_columns[index])
				else:
					temp_columns[index] = str(temp_columns[index]).rstrip(' ')
				index = index + 1
			customerID = self.search_for_customer_id(temp_columns)
			print customerID
			if customerID != 'AAAA':
				self.update_orders_with_tracking(customerID,temp_columns)
				self.insert_matrack_into_db(customerID,temp_columns)

		csv_file.close()
		#shutil.move("./CSVs/%s" %self.filename, "./CSV_ARCHIVE/%s-%s" %(self.filename,self.current_time))

	def search_for_customer_id(self, temp_columns):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			Failed_message = "Failed to connect to DB"
			print Failed_message
			self.send_email(Failed_message,temp_columns)
			cursor.close()
			cnx.close()
			exit(5)

		try:
			cursor.execute("SELECT customerID "
						   "FROM Orders "
						   "WHERE po_number = 'PO-%s' limit 1" %(temp_columns[0]))
			customerID = cursor.fetchone()
			cursor.close()
			cnx.close()
			return customerID
		except:
			print "Couldnt find customerID in function search_for_customer_id"
			cursor.close()
			cnx.close()
			customerID = 'AAAA'
			return customerID

	def update_orders_with_tracking(self,customerID,temp_columns):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function update_db_processed_xml"
			exit(5)
		try:
			cursor.execute("UPDATE Orders "
							   "SET tracking_number_received = 1, "
							   "tracking_number = '%s' "
							   "WHERE po_number = 'PO-%s' "
							   "AND customerID = '%s'" %(temp_columns[1],temp_columns[0],customerID[0]))
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print "Unable to update DB with xml_being_processed"
			print temp_columns
			cursor.close()
			cnx.close()
			return

	def insert_matrack_into_db(self,customerID,temp_columns):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function insert_matrack_into_db"
			exit(5)

		try:
			cursor.execute("INSERT INTO Tracking_Numbers "
						   "(po_number,tracking_number,detail_line_type,account_number,"
						   "shipping_cost,total_cost_parts,sbc_reference_number,date,"
						   "clerk_codes,shipping_type,customerID) "
						   "VALUES ('PO-%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
						   %(temp_columns[0],temp_columns[1],temp_columns[2],temp_columns[3],
							 temp_columns[4],temp_columns[5],temp_columns[6],temp_columns[7],
							 temp_columns[8],temp_columns[9],customerID[0]))
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print "Unable to insert tracking number from matrack as the record exists already"
			print temp_columns
			return

	def send_email(self,failed_message,*args):
		to = 'mathewusher@gmail.com'
		gmail_user = 'amazonordercheck@gmail.com'
		gmail_pwd = 'Jakewas6'
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(gmail_user,gmail_pwd)
		header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:Check Amazon Order \n'
		msg = header + '\n' + failed_message + '\t'
		smtpserver.sendmail(gmail_user, to, msg)
		smtpserver.close()
