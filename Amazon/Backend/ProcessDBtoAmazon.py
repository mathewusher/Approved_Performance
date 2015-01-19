#!/usr/bin/python2.7
from ftplib import FTP
import smtplib
import os
import mysql.connector
import shutil
from datetime import datetime
import time

class ProcessDBtoAmazon:
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
		self.homedir = '/home/musher/Approved_Performance/Approved_Performance/Amazon/Backend'
		#self.homedir = '/home/Amazon/Amazon'

	def main_logic(self):
		self.write_amazon_shipping_confirmation()
		#self.puttxtftp()

	def puttxtftp(self):
		'''This function is to put the txt file back into the /sbc/production/outbound folder on
		Approved Performances ftp server'''

		# Try to connect to the FTP server if not send e-mail to alert about ftp issue"
		try:
			ftp = FTP('%s' % self.ftpIP, timeout=5)
			ftp.login(user='%s' % self.ftpUser, passwd='%s' % self.ftpPassword)
		except:
			Failed_message = 'Unable to connect to FTP server in function puttxtftp'
			self.send_email(Failed_message)
			return

		# Change to correct directory on ftp server
		ftp.cwd("/sbc/production/outgoing")

		# Check to see if the archive folder exists, if not create it
		if 'TXT_ARCHIVE' not in ftp.nlst():
			ftp.mkd('TXT_ARCHIVE')

		# Change to the directory where the .txt files are located locally and read them into a list
		os.chdir("%s/TXTs" %self.homedir)
		txt_files = os.listdir("./")

		# Loop through the file and store them on the ftp server. Also move them into the archive folder locally
		for file in txt_files:
			ftp.storbinary("STOR " + file, open(file, 'rb'), 1024)
			shutil.move(file, '../TXT_ARCHIVE/%s' %file)

		# Close the ftp connection
		ftp.close()

	def write_amazon_shipping_confirmation(self):
		'''This function is to write out all the orders with tracking numbers flag set to true but amazon_ship_confirm
		set to false in the database'''

		# Try to connect to the database if not fail and notify
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			Failed_message =  "Failed to connect to DB"
			self.send_email(Failed_message)
			cursor.close()
			cnx.close()
			exit(4)

		# Try to query database for all orders that have a tracking number but do not have a txt file generated for
		# Amazon to consume on the ftp server

		try:
			cursor.execute("SELECT Orders.AmazonOrderID,Orders.AmazonOrderItemCode,Orders.Quantity,"
						   "Tracking_Numbers.date,Tracking_Numbers.shipping_type,Tracking_Numbers.tracking_number "
						   "FROM Orders "
						   "INNER JOIN Tracking_Numbers "
						   "ON Orders.po_number = Tracking_Numbers.po_number "
						   "WHERE Orders.tracking_number_received = '1' AND Orders.amazon_ship_confirm = '0'")
			items_to_report_to_amazon = cursor.fetchall()
			cursor.close()
			cnx.close()
		except:
			Failed_message =  "Unable to query database in function write_amazon_shipping_confirmation"
			self.send_email(Failed_message)
			cursor.close()
			cnx.close()
			return

		# If items_to_report_to_amazon has no matches simply return as there is nothing to process
		if not items_to_report_to_amazon:
			return

		# Change directory to path of application
		os.chdir(self.homedir)

		# try to open a file for writing if not send error report
		try:
			file_handle = open("./TXTs/amazon_ship_confirm.%s.txt" %(self.current_time), 'w')
		except:
			Failed_message = "Unable to open txt file for writing for amazon tracking information"
			self.send_email(Failed_message)
			return

		# Loop through all the items in the query that came back and write to open file
		# Update DB flag amazon_ship_confirm to 1 ( True ) so we don't pick it up again in next query
		for item in items_to_report_to_amazon:
			file_handle.write("%s\t%s\t%s\t%s\t%s\t%s\t \t%s\n" %(item[0],item[1],item[2],item[3],
																  item[4][:6],item[5][11:],item[4][5:]))
			self.update_amazon_ship_confirm(item)

		# Don't forget to close the file
		file_handle.close()

	def update_amazon_ship_confirm(self,item):
		'''This function is to update the individual the database flag amazon_ship_confirm for table Orders
		to 1 ( True ), it accepts 1 item'''

		# Try to connect to the database if not fail and send e-mail
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			Failed_message =  "Failed to connect to DB"
			self.send_email(Failed_message)
			cursor.close()
			cnx.close()
			exit(4)

		# Update the DB in table Orders based on the item that was passed into this function
		try:
			cursor.execute("UPDATE Orders "
						   "SET amazon_ship_confirm = '1' "
						   "WHERE AmazonOrderID = '%s' "
						   "AND AmazonOrderItemCode = '%s'" %(item[0],item[1]))
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print "This Order could not be updated to reflect Amazon shipping confirmation"
			cursor.close()
			cnx.close()


	def send_email(self,failed_message,*args):
		'''This function sends an email out to notify of issues, it accepts a failed_message str'''

		to = 'mathewusher@gmail.com'
		gmail_user = 'amazonordercheck@gmail.com'
		gmail_pwd = 'Jakewas6'
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(gmail_user,gmail_pwd)
		header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:Check Report Back to Amazon \n'
		msg = header + '\n' + failed_message
		smtpserver.sendmail(gmail_user, to, msg)
		smtpserver.close()
