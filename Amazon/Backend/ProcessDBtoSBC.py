#!/usr/bin/python 2.7
import sys
import os
import mysql.connector
import shutil
import glob
import smtplib
from ftplib import FTP
from decimal import *

class ProcessDBtoSBC:
	def __init__(self, ftpIP, ftpUser, ftpPassword):
		self.ftpIP = ftpIP
		self.ftpUser = ftpUser
		self.ftpPassword = ftpPassword

		self.dbuser = 'root'
		self.dbhost = '172.16.3.65'
		self.database = 'Approved_Performance'
		self.dbpassword = 'PLOK1234plok'
		self.homedir = '/home/musher/Approved_Performance/Approved_Performance/Amazon/Backend'
#		self.homedir = '/home/Amazon/Amazon'

		self.xml_start = '<?xml version="1.0" encoding="utf-8" ?>'
		self.order_start = '<SBCPartOrderRequest>'
		self.tracking_info_start = '<TrackingInfo>'
		self.tracknum_start = '<TrackNum>'
		self.tracknum_end = '</TrackNum>'
		self.tracking_info_stop = '</TrackingInfo>'
		self.buyer_info_start = '<BuyerInfo>'
		self.customer_id_start = '<CustomerID>'
		self.customer_id_stop = '</CustomerID>'
		self.password = '<Password>9265</Password>'
		self.password_start = '<Password>'
		self.password_stop = '</Password>'
		self.buyer_info_stop = '</BuyerInfo>'
		self.selling_store = '<SellingStore>1</SellingStore>'
		self.selling_store_start = '<SellingStore>'
		self.selling_store_stop = '</SellingStore>'
		self.ponum_start = '<PONum>'
		self.ponum_stop = '</PONum>'
		self.cancel_order_flag = '<CancelOrderFlag>N</CancelOrderFlag>'
		self.cancel_order_flag_start = '<CancelOrderFlag>'
		self.cancel_order_flag_stop = '</CancelOrderFlag>'
		self.job_number_start = '<JobNumber>'
		self.job_number_stop = '</JobNumber>'
		self.use_sell_price = '<UseSellPrice>Y</UseSellPrice>'
		#self.use_sell_price_start = '<UseSellPrice>'
		#self.use_sell_price_stop = '</UseSellPrice>'
		self.items_start = '<Items>'
		self.item_start = '<Item>'
		self.item_id_start = '<ItemID>'
		self.item_id_stop = '</ItemID>'
		self.mfg_code_start = '<MfgCode>'
		self.mfg_code_stop = '</MfgCode>'
		self.part_num_start = '<PartNum>'
		self.part_num_stop = '</PartNum>'
		self.qty_start = '<Qty>'
		self.qty_stop = '</Qty>'
		self.qty_order_start = '<QtyOrder>'
		self.qty_order_end = '</QtyOrder>'
		self.sell_price_start = '<SellPrice>'
		self.sell_price_stop = '</SellPrice>'
		self.item_stop = '</Item>'
		self.items_stop = '</Items>'
		self.sold_to_start = '<SoldTo>'
		self.sold_to_company_name_start = '<CompanyName>'
		self.sold_to_company_name_stop= '</CompanyName>'
		self.sold_to_street_start= '<Street>'
		self.sold_to_street_stop = '</Street>'
		self.sold_to_city_start = '<City>'
		self.sold_to_city_stop = '</City>'
		self.sold_to_state_start = '<State>'
		self.sold_to_state_stop = '</State>'
		self.sold_to_zip_code_start = '<ZipCode>'
		self.sold_to_zip_code_stop = '<ZipCode>'
		self.sold_to_phone_number_start = '<Phone>'
		self.sold_to_phone_number_stop = '</Phone>'
		self.sold_to_stop = '</SoldTo>'
		self.ship_to_start = '<ShipTo>'
		self.ship_to_company_name_start = '<CompanyName>'
		self.ship_to_company_name_end = '</CompanyName>'
		self.ship_to_last_name_start = '<LastName>'
		self.ship_to_last_name_end = '</LastName>'
		self.ship_to_street_start = '<Street>'
		self.ship_to_street_end = '</Street>'
		self.ship_to_city_start = '<City>'
		self.ship_to_city_end = '</City>'
		self.ship_to_state_start = '<State>'
		self.ship_to_state_end = '</State>'
		self.ship_to_zip_code_start = '<ZipCode>'
		self.ship_to_zip_code_end = '</ZipCode>'
		self.ship_to_phone_number_start = '<Phone>'
		self.ship_to_phone_number_end = '</Phone>'
		self.ship_to_stop = '</ShipTo>'
		self.ship_via = '<ShipVia>F</ShipVia>'
		self.order_stop = '</SBCPartOrderRequest>'

	def upload_xml_to_ftp(self):
		try:
			ftp = FTP('%s' % self.ftpIP, timeout=5)
			ftp.login(user='%s' % self.ftpUser, passwd='%s' % self.ftpPassword)
		except:
			print "Unable to connect to FTP site"
			return

		ftp.cwd("/sbc/amazon/new_inbound")
		os.chdir("%s/XMLs" %self.homedir)
		xml_files = os.listdir("./")
		for file in xml_files:
			ftp.storbinary("STOR " + file, open(file, 'rb'), 1024)
			shutil.move(file, '%s/XML_ARCHIVE/%s' %(self.homedir,file))

		ftp.close()



	def main_logic(self):
		rows = self.search_for_orders_not_processed()
		for amazonorderid in rows:
			number_of_items = self.get_number_of_items_in_order(amazonorderid)
			unique_accounts = self.get_unique_accounts_in_order(amazonorderid)
			job_number_count = len(unique_accounts)
			job_number = 1
			for account in unique_accounts:
				items_in_order = self.get_items_in_order(amazonorderid,account)
				customerid = items_in_order[0][3]
				customer_information = self.get_customer_information(customerid)

				SKU_list = []
				QUANTITY_OF_SKU_list = []
				TOTAL_AMOUNT_OF_ITEM_list = []
				CUSTOMER_ID_LIST = []
				SOLD_TO_COMPANY_NAME_LIST = []
				SOLD_TO_STREET_ADDRESS_LIST = []
				SOLD_TO_CITY_LIST = []
				SOLD_TO_STATE_LIST = []
				SOLD_TO_ZIP_CODE_LIST = []
				SOLD_TO_PHONE_NUMBER_LIST = []
				index = 0
				#while index < len(items_in_order):
				for item in items_in_order:
					SKU_list.append(item[0])
					QUANTITY_OF_SKU_list.append(int(item[1]))
					TOTAL_AMOUNT_OF_ITEM_list.append(Decimal(item[2]))
					CUSTOMER_ID_LIST.append(item[4])
					SOLD_TO_COMPANY_NAME_LIST.append(item[5])
					SOLD_TO_STREET_ADDRESS_LIST.append(item[6])
					SOLD_TO_CITY_LIST.append(item[7])
					SOLD_TO_STATE_LIST.append(item[8])
					SOLD_TO_ZIP_CODE_LIST.append(item[9])
					SOLD_TO_PHONE_NUMBER_LIST.append(item[10])

				index =  0
				PRICE_FOR_ITEM = []
				while index < len(items_in_order):
					PRICE = TOTAL_AMOUNT_OF_ITEM_list[index] / QUANTITY_OF_SKU_list[index]
					PRICE_FOR_ITEM.append(PRICE)
					index = index + 1

				part_number_list = []
				mfg_code_list = []
				for SKU in SKU_list:
					mfg_code_list.append(SKU[:3])
					part_number_list.append(SKU[3:])

				#STATE = self.get_2_char_state(customer_information[5])
				purchase_order_number = self.write_xml_to_sbc(amazonorderid,number_of_items,items_in_order,
							 customer_information,SKU_list,QUANTITY_OF_SKU_list,
							 TOTAL_AMOUNT_OF_ITEM_list,CUSTOMER_ID_LIST,
							 SOLD_TO_COMPANY_NAME_LIST, SOLD_TO_STREET_ADDRESS_LIST,
							 SOLD_TO_CITY_LIST,SOLD_TO_STATE_LIST,SOLD_TO_ZIP_CODE_LIST,
							 SOLD_TO_PHONE_NUMBER_LIST,PRICE_FOR_ITEM,
							 mfg_code_list,part_number_list,job_number,job_number_count)
				job_number = job_number + 1
				self.update_db_processed_xml(amazonorderid,account,purchase_order_number)
#				self.upload_xml_to_ftp()


	def write_xml_to_sbc(self,amazonorderid,number_of_items,items_in_order,
						 customer_information,SKU_list,QUANTITY_OF_SKU_list,
						 TOTAL_AMOUNT_OF_ITEM_list,CUSTOMER_ID_LIST,
						 SOLD_TO_COMPANY_NAME_LIST, SOLD_TO_STREET_ADDRESS_LIST,
						 SOLD_TO_CITY_LIST,SOLD_TO_STATE_LIST,SOLD_TO_ZIP_CODE_LIST,
						 SOLD_TO_PHONE_NUMBER_LIST,PRICE_FOR_ITEM,
						 mfg_code_list,part_number_list,job_number,job_number_count):
		os.chdir(self.homedir)

		failed_message = ''
		if job_number_count > 1:
			ordernumber = job_number
			if os.path.isfile('./XMLs/PO-%s-%s.xml' %(amazonorderid[0],ordernumber)):
				print "file exists"
				return
			else:
				xml_file = open('./XMLs/PO-%s-%s.xml' %(amazonorderid[0], ordernumber), 'w')
			purchase_order_number = 'PO-%s-%s' %(amazonorderid[0], ordernumber)
		else:
			if os.path.isfile('./XMLs/PO-%s.xml' %(amazonorderid)):
				print "file exists"
				return
			else:
				xml_file = open('./XMLs/PO-%s.xml' %(amazonorderid), 'w')
			purchase_order_number = 'PO-%s' %(amazonorderid)

		xml_file.write("%s\n" %(self.xml_start))
		xml_file.write("%s\n" %(self.order_start))
		xml_file.write("\t%s\n" %(self.tracking_info_start))
		xml_file.write("\t\t%s%s%s\n" %(self.tracknum_start,amazonorderid[0][:11],self.tracknum_end))
		xml_file.write("\t%s\n" %(self.tracking_info_stop))
		xml_file.write("\t%s\n" %(self.buyer_info_start))
		xml_file.write("\t\t%s%s%s\n" %(self.customer_id_start,CUSTOMER_ID_LIST[0],self.customer_id_stop))
		xml_file.write("\t\t%s\n" %(self.password))
		xml_file.write("\t%s\n" %(self.buyer_info_stop))
		xml_file.write("\t%s\n" %(self.selling_store))
		xml_file.write("\t%s%s%s\n" %(self.ponum_start,amazonorderid[0][:11],self.ponum_stop))
		xml_file.write("\t%s\n" %(self.cancel_order_flag))
		if job_number_count > 1:
			xml_file.write("\t%s%s-%s%s\n" %(self.job_number_start,amazonorderid[0][11:],job_number,self.job_number_stop))
		else:
			xml_file.write("\t%s%s%s\n" %(self.job_number_start,amazonorderid[0][11:],self.job_number_stop))
		xml_file.write("\t%s\n" %(self.use_sell_price))
		xml_file.write("\t%s\n" %(self.items_start))
		index = 0
		item_count = 1
		for item in items_in_order:
			xml_file.write("\t\t%s\n" %(self.item_start))
			xml_file.write("\t\t\t%s%s%s\n" %(self.item_id_start,item_count,self.item_id_stop))
			xml_file.write("\t\t\t\t%s%s%s\n" %(self.mfg_code_start,mfg_code_list[index],self.mfg_code_stop))
			xml_file.write("\t\t\t\t%s%s%s\n" %(self.part_num_start,part_number_list[index],self.part_num_stop))
			xml_file.write("\t\t\t\t%s%s%s\n" %(self.qty_start,QUANTITY_OF_SKU_list[index],self.qty_stop))
			xml_file.write("\t\t\t\t%s%s%s\n" %(self.qty_order_start,QUANTITY_OF_SKU_list[index],self.qty_order_end))
			xml_file.write("\t\t\t\t%s%s%s\n" %(self.sell_price_start,PRICE_FOR_ITEM[index],self.sell_price_stop))
			xml_file.write("\t\t%s\n" %(self.item_stop))
			index = index + 1
			item_count = item_count + 1
		xml_file.write("\t%s\n" %(self.items_stop))
		xml_file.write("\t%s\n" %(self.sold_to_start))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_company_name_start,SOLD_TO_COMPANY_NAME_LIST[0],self.sold_to_company_name_stop))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_street_start,SOLD_TO_STREET_ADDRESS_LIST[0],self.sold_to_street_stop))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_city_start,SOLD_TO_CITY_LIST[0],self.sold_to_city_stop))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_zip_code_start,SOLD_TO_ZIP_CODE_LIST[0],self.sold_to_zip_code_stop))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_state_start,SOLD_TO_STATE_LIST[0],self.sold_to_state_stop))
		xml_file.write("\t\t%s%s%s\n" %(self.sold_to_phone_number_start,SOLD_TO_PHONE_NUMBER_LIST[0],self.sold_to_phone_number_stop))
		xml_file.write("\t%s\n" %(self.sold_to_stop))
		xml_file.write("\t%s\n" %(self.ship_to_start))
		xml_file.write("\t\t%s%s%s\n" %(self.ship_to_company_name_start,customer_information[0],self.ship_to_company_name_end))
		total_length_address = 0
		try:
			total_length_address = len(customer_information[2]) + len(customer_information[3])
			complete_address = customer_information[2] + '' + customer_information[3]
		except:
			total_length_address = len(customer_information[2])
			complete_address = customer_information[2]

		if total_length_address > 50:
			failed_message = "Total length of address of field 1 and 2 is greater than 50 characters"
		elif total_length_address > 25:
			failed_message = "Total length of address of field 1 and 2 is greater than 25 characters please investigate"
			xml_file.write("\t\t%s%s%s\n" %(self.ship_to_last_name_start,complete_address[25:],self.ship_to_last_name_end))
			xml_file.write("\t\t%s%s%s\n" %(self.ship_to_street_start,complete_address[:25],self.ship_to_street_end))
		else:
			xml_file.write("\t\t%s%s%s\n" %(self.ship_to_last_name_start,customer_information[3],self.ship_to_last_name_end))
			xml_file.write("\t\t%s%s%s\n" %(self.ship_to_street_start,customer_information[2],self.ship_to_street_end))
		xml_file.write("\t\t%s%s%s\n" %(self.ship_to_city_start,customer_information[4],self.ship_to_city_end))
		xml_file.write("\t\t%s%s%s\n" %(self.ship_to_state_start,customer_information[5],self.ship_to_state_end))
		xml_file.write("\t\t%s%s%s\n" %(self.ship_to_zip_code_start,customer_information[6],self.ship_to_zip_code_end))
		xml_file.write("\t\t%s%s%s\n" %(self.ship_to_phone_number_start,customer_information[1],self.ship_to_phone_number_end))
		xml_file.write("\t%s\n" %(self.ship_to_stop))
		xml_file.write("\t%s\n" %(self.ship_via))
		xml_file.write("%s" %(self.order_stop))
		xml_file.close()
		if len(str(customer_information[1]).strip('()+- ')) > 15:
			failed_message = failed_message + '\n Total length of phone number is greater than 15 characters'


		if failed_message != '':
			print failed_message
			print amazonorderid
			self.send_email(failed_message,amazonorderid)

		return purchase_order_number

	def send_email(self,failed_message,amazonorderid):
		to = 'mathewusher@gmail.com'
		gmail_user = 'amazonordercheck@gmail.com'
		gmail_pwd = 'Jakewas6'
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(gmail_user,gmail_pwd)
		header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:Check Amazon Order \n'
		msg = header + '\n' + failed_message + '\t' + amazonorderid[0]
		smtpserver.sendmail(gmail_user, to, msg)
		smtpserver.close()

	def update_db_processed_xml(self,amazonorderid,account,purchase_order_number):
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
						   "SET sbc_xml_generated = 1, "
						   "po_number = '%s' "
						   "WHERE AmazonOrderID = '%s' "
						   "AND account_number = '%s'" %(purchase_order_number,amazonorderid[0],account[0]))
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print "Unable to update DB with xml_being_processed"
			cursor.close()
			cnx.close()
			exit(4)

	def search_for_customer(self,buyer_data_list):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function search_for_customer"
			exit(5)
		try:
			tuple_of_search_customer = tuple(buyer_data_list[:3])
			temp_search = "SELECT customerID FROM Customer WHERE BuyerEmailAddress = %s " \
						  "AND BuyerName = %s AND BuyerPhoneNumber = %s limit 1"
			cursor.execute(temp_search, tuple_of_search_customer)
			row = cursor.fetchone()
			customer_ID = str(row).strip('(),')
			cursor.close()
			cnx.close()
			return customer_ID
		except:
			print "Did not find the customer in function search_for_customer"
			cursor.close()
			cnx.close()

	def get_customer_information(self,customerid):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function get_customer_information"
			exit(5)

		try:
			cursor.execute("SELECT BuyerName,BuyerPhoneNumber,AddressFieldOne,AddressFieldTwo,"
						   "City,StateOrRegion,PostalCode "
						   "FROM Customer WHERE customerID = '%s'" %(customerid))
			customer_information = cursor.fetchone()
			cursor.close()
			cnx.close()
			return customer_information
		except:
			print "Unable to get customer information in function get_customer_information"
			cursor.close()
			cnx.close()
			exit(2)

	def get_items_in_order(self,amazonorderid,account):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function get_items_in_order"
			exit(5)

		try:
			cursor.execute("SELECT Orders.SKU, Orders.QUANTITY, Orders.ItemAmount ,Orders.customerID, "
						   "mfg_to_account_number.account_number, mfg_to_account_number.sold_to_company_name, "
						   "mfg_to_account_number.sold_to_street_address, mfg_to_account_number.sold_to_city, "
						   "mfg_to_account_number.sold_to_state, mfg_to_account_number.sold_to_zip_code, "
						   "mfg_to_account_number.sold_to_phone_number FROM Orders INNER JOIN mfg_to_account_number "
						   "ON Orders.account_number = mfg_to_account_number.ID "
						   "WHERE AmazonOrderID = '%s' AND Orders.account_number = '%s'" %(amazonorderid[0],account[0]))
			items = cursor.fetchall()
			cursor.close()
			cnx.close()
			return items
		except:
			print "Failed to get SKU and Quantity from Orders"
			cursor.close()
			cnx.close()
			pass

	def get_unique_accounts_in_order(self,amazonorderid):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function get_unique_accounts_in_order"
			exit(5)

		try:
			cursor.execute("SELECT DISTINCT account_number FROM Orders WHERE AmazonOrderID = '%s'" %(amazonorderid))
			items = cursor.fetchall()
			cursor.close()
			cnx.close()
			return items
		except:
			print "Failed to get SKU and Quantity from Orders"
			cursor.close()
			cnx.close()
			pass

	def get_number_of_items_in_order(self,amazonorderid):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function get_number_of_items_in_order"
			exit(5)

		try:
			cursor.execute("SELECT COUNT(*) FROM Orders WHERE AmazonOrderID = '%s'" %(amazonorderid))
			number_of_items = cursor.fetchone()[0]
			cursor.close()
			cnx.close()
			return number_of_items
		except:
			print "Query did not work"
			cursor.close()
			cnx.close()
			exit(1)

	def search_for_orders_not_processed(self):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function search_for_orders_not_processed"
			exit(5)


		try:
			orders_not_processed_query = "SELECT DISTINCT AmazonOrderID FROM Orders WHERE sbc_xml_generated = '0'"
			cursor.execute(orders_not_processed_query)
		except:
			print "Query did not work"
			cursor.close()
			cnx.close()
			exit(3)

		rows = cursor.fetchall()
		orders_not_processed_list = []
		temp_list = []
		for row in rows:
			temp_list.append(list(row))

		orders_not_processed_list = sorted(temp_list)
		cursor.close()
		cnx.close()
		return rows

	def search_for_mfg_information(self,order_mfg, order_marketplace):
		mfg_tuple = (order_mfg, order_marketplace)
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function search_for_mfg_information"
			exit(5)



		try:
			mfg_code_search = "SELECT account_number,sold_to_company_name,sold_to_street_address,sold_to_city," \
							  "sold_to_state,sold_to_zip_code,sold_to_phone_number " \
							  "FROM mfg_to_account_number " \
							  "WHERE mfg = %s and marketplace = %s "
			cursor.execute(mfg_code_search, mfg_tuple)
			manufacturer_information = cursor.fetchone()
			return manufacturer_information
		except:
			print "Manufacturer does not exist in table mfg_to_account_number"
			exit(2)


	def search_orders_by_customer(self):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function search_orders_by_customer"
			exit(5)

		customer_order_search = "SELECT Customer.BuyerName, Customer.BuyerPhoneNumber, Customer.AddressFieldOne, " \
								"Customer.AddressFieldTwo, Customer.City, Customer.StateOrRegion, Customer.PostalCode, " \
								"Customer.CountryCode Orders.Title FROM Customer INNER" \
								" JOIN Orders on Customer.customerID = Orders.customerID WHERE Orders.customerID = '28'"
		cursor.execute(customer_order_search)
		rows = cursor.fetchall()
		print len(rows)
		for row in rows:
			print row
