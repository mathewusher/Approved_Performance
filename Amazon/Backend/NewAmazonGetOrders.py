#!/usr/bin/python2.7
from ftplib import FTP
import sys
import os
import mysql.connector
import xmltodict
import shutil
import glob
import re
from decimal import *


class NewAmazonGetOrders:
	def __init__(self, ftpIP, ftpUser, ftpPassword):
		self.ftpIP = ftpIP
		self.ftpUser = ftpUser
		self.ftpPassword = ftpPassword
		self.list_of_files = []
		self.list_of_elements = ['AmazonOrderID', 'AmazonSessionID', 'OrderDate', 'OrderPostedDate']
		self.billing_data_list = ['BuyerEmailAddress', 'BuyerName', 'BuyerPhoneNumber']
		self.FulfillmentData_list = ['FulfillmentMethod', 'FulfillmentServiceLevel']
		self.address_list = ['Name', 'AddressFieldOne', 'AddressFieldTwo', 'City', 'StateOrRegion', 'PostalCode', 'CountryCode',
							 'PhoneNumber']
		self.dbuser = 'root'
		self.dbhost = '172.16.3.65'
		self.database = 'Approved_Performance'
		self.dbpassword =  'PLOK1234plok'
		self.homedir = '/home/musher/Approved_Performance/Approved_Performance/Amazon/Backend'
#		self.homedir = '/home/Amazon/Amazon'

	def Amazonftpget(self):
		os.chdir(self.homedir)
		try:
			ftp = FTP('%s' % self.ftpIP, timeout=5)
			ftp.login(user='%s' % self.ftpUser, passwd='%s' % self.ftpPassword)
			ftp.cwd("/sbc/production/reports")
			ftp_list_of_files = ftp.nlst()
			if 'ARCHIVE' not in ftp.nlst():
				ftp.mkd('ARCHIVE')
			ftp.close()
		except:
			print "Unable to connect to FTP site"

		for filename in ftp_list_of_files:
			if filename.endswith('xml'):
				if os.path.exists('./NEWORDERS/%s' %(filename)):
					print "File exists"
					pass
				else:
					local_file = open('./NEWORDERS/%s' %(filename), 'w')
					try:
						ftp = FTP('%s' % self.ftpIP, timeout=5)
						ftp.login(user='%s' % self.ftpUser, passwd='%s' % self.ftpPassword)
						ftp.cwd("/sbc/production/reports")
						ftp.retrbinary('RETR ' + filename, local_file.write)
						local_file.close()
						self.list_of_files.append(filename)
					except:
						print "%s had error" %(filename)
						pass
					local_file.close()
					statinfo = os.stat('./NEWORDERS/%s' %(filename))
					if statinfo.st_size == 0:
						print "0 Byte file"
						os.remove('./NEWORDERS/%s' %(filename))
						ftp.close()
						pass
					else:
						ftp.rename(filename, "./ARCHIVE/%s" %(filename))
						ftp.close()
			else:
				pass

	def Add_xml_to_list(self):
		os.chdir('%s/NEWORDERS' %self.homedir)
		xml_files = os.listdir('./')
		for file in xml_files:
			self.list_of_files.append(file)

	def main_logic(self):
		#self.Amazonftpget()
		self.Add_xml_to_list()
		self.AmazonXML()

	def AmazonXML(self):
		for xmlfile in self.list_of_files:
			try:
				os.chdir('%s/NEWORDERS' %self.homedir)
				file_handle = open(xmlfile, 'r')
				doc = xmltodict.parse(file_handle)
			except:
				print "Unable to open file"
				break

			try:
				message_index = 0
				message_test_case = []
				message_test_case = doc['AmazonEnvelope']['Message'][message_index]
				while message_index < len(doc['AmazonEnvelope']['Message']):
					try:
						item_index = 0
						item_test_case = []
						item_test_case = doc['AmazonEnvelope']['Message'][message_index]['OrderReport']['Item'][item_index]
						while item_index < len(doc['AmazonEnvelope']['Message'][message_index]['OrderReport']['Item']):
							message_doc = []
							item_doc = []
							message_doc = doc['AmazonEnvelope']['Message'][message_index]
							item_doc = doc['AmazonEnvelope']['Message'][message_index]['OrderReport']['Item'][item_index]
							list_for_db = self.single_item_single_order(message_doc,item_doc)
							self.commit_to_DB(list_for_db)
							item_index = item_index + 1
					except:
						message_doc = []
						item_doc = []
						message_doc = doc['AmazonEnvelope']['Message'][message_index]
						item_doc = doc['AmazonEnvelope']['Message'][message_index]['OrderReport']['Item']
						list_for_db = self.single_item_single_order(message_doc,item_doc)
						self.commit_to_DB(list_for_db)
					message_index = message_index + 1
			except:
				try:
					item_index = 0
					item_test_case = []
					item_test_case = doc['AmazonEnvelope']['Message']['OrderReport']['Item'][item_index]
					while item_index < len(doc['AmazonEnvelope']['Message']['OrderReport']['Item']):
						message_doc = []
						item_doc = []
						message_doc = doc['AmazonEnvelope']['Message']
						item_doc = doc['AmazonEnvelope']['Message']['OrderReport']['Item'][item_index]
						list_for_db = self.single_item_single_order(message_doc,item_doc)
						self.commit_to_DB(list_for_db)
						item_index = item_index + 1
				except:
					message_doc = []
					item_doc = []
					message_doc = doc['AmazonEnvelope']['Message']
					item_doc = doc['AmazonEnvelope']['Message']['OrderReport']['Item']
					list_for_db = self.single_item_single_order(message_doc,item_doc)
					self.commit_to_DB(list_for_db)
			file_handle.close()
			shutil.move(xmlfile, '%s/INBOUND_ARCHIVE/%s' %(self.homedir,xmlfile))


	def single_item_single_order(self, message_handle, item_handle):
		message = message_handle
		item = item_handle
		new_list = []
		buyer_data_list = []
		customer_order_list = []
		for element in self.list_of_elements:
			try:
				new_list.append(str(message_handle['OrderReport'][element]))
				customer_order_list.append(str(message_handle['OrderReport'][element]))
			except:
				new_list.append('')
				customer_order_list.append('')
		for buyer_data in self.billing_data_list:
			try:
				new_list.append(str(message_handle['OrderReport']['BillingData'][buyer_data]))
				buyer_data_list.append(str(message_handle['OrderReport']['BillingData'][buyer_data]))
			except:
				new_list.append('')
				buyer_data_list.append('')
		for fulfillment in self.FulfillmentData_list:
			try:
				new_list.append(str(message_handle['OrderReport']['FulfillmentData'][fulfillment]))
				customer_order_list.append(str(message_handle['OrderReport']['FulfillmentData'][fulfillment]))
			except:
				new_list.append('')
				customer_order_list.append('')
		for address_file in self.address_list:
			try:
				new_list.append(str(message_handle['OrderReport']['FulfillmentData']['Address'][address_file]))
				buyer_data_list.append(str(message_handle['OrderReport']['FulfillmentData']['Address'][address_file]))
			except:
				new_list.append('')
				buyer_data_list.append('')

		self.commit_customer_to_db(buyer_data_list)
		customer_ID = self.search_for_customer(buyer_data_list)

		try:
			new_list.append(str(item_handle['AmazonOrderItemCode']))
			customer_order_list.append(str(item_handle['AmazonOrderItemCode']))
		except:
			new_list.append('')
			customer_order_list.append('')
		try:
			new_list.append(str(item_handle['SKU']))
			customer_order_list.append(str(item_handle['SKU']))
		except:
			new_list.append('')
			customer_order_list.append('')
		try:
			new_list.append(str(item_handle['Title']))
			customer_order_list.append(str(item_handle['Title']))
		except:
			new_list.append('')
			customer_order_list.append('')
		try:
			new_list.append(str(item_handle['Quantity']))
			customer_order_list.append(str(item_handle['Quantity']))
		except:
			new_list.append('')
			customer_order_list.append('')
		try:
			new_list.append(str(item_handle['ProductTaxCode']))
			customer_order_list.append(str(item_handle['ProductTaxCode']))
		except:
			new_list.append('')
			customer_order_list.append('')
		item_price_index = 0
		while item_price_index < 4:
			try:
				new_list.append(str(item_handle['ItemPrice']['Component'][item_price_index]['Type']))
				customer_order_list.append(str(item_handle['ItemPrice']['Component'][item_price_index]['Type']))
			except:
				new_list.append('')
				customer_order_list.append('')
			try:
				new_list.append(str(item_handle['ItemPrice']['Component'][item_price_index]['Amount']['#text']))
				customer_order_list.append(str(item_handle['ItemPrice']['Component'][item_price_index]['Amount']['#text']))
			except:
				new_list.append('')
				customer_order_list.append('')
			item_price_index = item_price_index + 1
		try:
			new_list.append(str(item_handle['ItemFees']['Fee']['Type']))
			customer_order_list.append(str(item_handle['ItemFees']['Fee']['Type']))
		except:
			new_list.append('')
			customer_order_list.append('')
		try:
			new_list.append(str(item_handle['ItemFees']['Fee']['Amount']['#text']))
			customer_order_list.append(str(item_handle['ItemFees']['Fee']['Amount']['#text']))
		except:
			new_list.append('')
			customer_order_list.append('')
		promotion_index = 0
		while promotion_index < 4:
			try:
				new_list.append(str(item_handle['Promotion'][promotion_index]['PromotionClaimCode']))
				new_list.append(str(item_handle['Promotion'][promotion_index]['MerchantPromotionID']))
				customer_order_list.append(str(item_handle['Promotion'][promotion_index]['PromotionClaimCode']))
				customer_order_list.append(str(item_handle['Promotion'][promotion_index]['MerchantPromotionID']))
				component_index = 0
				while component_index < len(item_handle['Promotion'][promotion_index]['Component']):
					new_list.append(str(item_handle['Promotion'][promotion_index]['Component'][component_index]['Type']))
					new_list.append(str(item_handle['Promotion'][promotion_index]['Component'][component_index]['Amount']['#text']))
					customer_order_list.append(str(item_handle['Promotion'][promotion_index]['Component'][component_index]['Type']))
					customer_order_list.append(str(item_handle['Promotion'][promotion_index]['Component'][component_index]['Amount']['#text']))
					component_index = component_index + 1
			except:
				new_list.extend(['','','','','',''])
				customer_order_list.extend(['','','','','',''])
			promotion_index = promotion_index + 1
		try:
			new_list.append(str(item_handle['ExpectedShipDateRange']['EarliestShipDate']))
			new_list.append(str(item_handle['ExpectedShipDateRange']['LatestShipDate']))
			customer_order_list.append(str(item_handle['ExpectedShipDateRange']['EarliestShipDate']))
			customer_order_list.append(str(item_handle['ExpectedShipDateRange']['LatestShipDate']))
		except:
			new_list.extend(['',''])
			customer_order_list.extend(['',''])
		try:
			new_list.append(str(item_handle['ExpectedDeliveryDateRange']['EarliestDeliveryDate']))
			new_list.append(str(item_handle['ExpectedDeliveryDateRange']['LatestDeliveryDate']))
			customer_order_list.append(str(item_handle['ExpectedDeliveryDateRange']['EarliestDeliveryDate']))
			customer_order_list.append(str(item_handle['ExpectedDeliveryDateRange']['LatestDeliveryDate']))
		except:
			new_list.extend(['',''])
			customer_order_list.extend(['',''])
		self.insert_customer_order(customer_ID,customer_order_list)
		return new_list


	def search_account_number_id(self, mfg, marketplace):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Failed to connect to DB"
			cursor.close()
			cnx.close()
			exit(4)

		try:
			cursor.execute("SELECT ID FROM mfg_to_account_number "
						   "WHERE mfg = '%s' AND marketplace = '%s'" %(mfg,marketplace))
			account_number = cursor.fetchone()
			cursor.close()
			cnx.close()
			return account_number
		except:
			print "Couldnt retrieve account_number"
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
			exit(4)
		try:
			tuple_of_search_customer = tuple(buyer_data_list[:3])
			temp_search = "SELECT customerID FROM Customer WHERE BuyerEmailAddress = %s AND BuyerName = %s AND BuyerPhoneNumber = %s limit 1"
			cursor.execute(temp_search, tuple_of_search_customer)
			row_list = []
			row = cursor.fetchone()
			customer_ID = str(row).strip('(),')
			cursor.close()
			cnx.close()
			return customer_ID
		except:
			print "Did not find the customer"
			cursor.close()
			cnx.close()

	def insert_customer_order(self,customer_ID,customer_order_list):
		customer_order_list.append(customer_ID)
		mfg = customer_order_list[7][:3]
		account_number = self.search_account_number_id(mfg, 'amazon')
		customer_order_list.append(account_number[0])
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function insert_customer_order"
			exit(4)

		index_list = [12,14,16,18,20,24,26,30,32,36,38,42,44]
		for index in index_list:
			if customer_order_list[index] == '':
				customer_order_list[index] = '0.00'
			customer_order_list[index] = Decimal(customer_order_list[index])

		tuple_of_order = tuple(customer_order_list)
		new_tuple = ('AmazonOrderID','AmazonSessionID','OrderDate','OrderPostedDate','FulfillmentMethod','FulfillmentServiceLevel','AmazonOrderItemCode','SKU','Title','Quantity','ProductTaxCode','ItemType','ItemAmount','ShippingType','ShippingAmount','ItemTaxType','ItemTaxAmount','ShippingTaxType','ShippingTaxAmount','ItemFeeType','ItemFeeAmount','PromotionClaimCode','MerchantPromotionID','PromotionType','PromotionAmount','PromotionShippingType','PromotionShippingAmount','Promotion2ClaimCode','MerchantPromotionID2','Promotion2Type','Promotion2Amount','Promotion2ShippingType','Promotion2ShippingAmount','Promotion3ClaimCode','MerchantPromotionID3','Promotion3Type','Promotion3Amount','Promotion3ShippingType','Promotion3ShippingAmount','Promotion4ClaimCode','MerchantPromotionID4','Promotion4Type','Promotion4Amount','Promotion4ShippingType','Promotion4ShippingAmount','EarliestShipDate','LatestShipDate','EarliestDeliveryDate','LatestDeliveryDate','customerID')
		add_order_to_customer = ("INSERT INTO Orders " "(AmazonOrderID,AmazonSessionID,OrderDate,OrderPostedDate,FulfillmentMethod,FulfillmentServiceLevel,AmazonOrderItemCode,SKU,Title,Quantity,ProductTaxCode,ItemType,ItemAmount,ShippingType,ShippingAmount,ItemTaxType,ItemTaxAmount,ShippingTaxType,ShippingTaxAmount,ItemFeeType,ItemFeeAmount,PromotionClaimCode,MerchantPromotionID,PromotionType,PromotionAmount,PromotionShippingType,PromotionShippingAmount,Promotion2ClaimCode,MerchantPromotionID2,Promotion2Type,Promotion2Amount,Promotion2ShippingType,Promotion2ShippingAmount,Promotion3ClaimCode,MerchantPromotionID3,Promotion3Type,Promotion3Amount,Promotion3ShippingType,Promotion3ShippingAmount,Promotion4ClaimCode,MerchantPromotionID4,Promotion4Type,Promotion4Amount,Promotion4ShippingType,Promotion4ShippingAmount,EarliestShipDate,LatestShipDate,EarliestDeliveryDate,LatestDeliveryDate,customerID,account_number) " "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
		try:
			cursor.execute(add_order_to_customer, tuple_of_order)
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print 'Duplicate Order Item'
			cursor.close()
			cnx.close()
			pass

	def update_state_2_char(self,zip_code, buyer_data_list):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()

		except:
			print "Unable to connect to DB in function update_state_2_char"
			exit(4)
		try:
			cursor.execute("SELECT state "
						   "FROM zip_codes "
						   "WHERE zip = '%s'" %(zip_code))
			row = cursor.fetchone()[0]
			STATE = str(row).strip('(),')
			cursor.close()
			cnx.close()
			return STATE
		except:
			failed_message = "State lookup failed"
			self.send_email(failed_message, buyer_data_list)
			cursor.close()
			cnx.close()

	def commit_customer_to_db(self,buyer_data_list):
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function commit_customer_to_db"
			exit(4)
		if len(buyer_data_list) == 11:
			if len(buyer_data_list[8]) > 5:
				zip_code = buyer_data_list[8][:5]
			else:
				zip_code = buyer_data_list[8]
			buyer_data_list[7] = self.update_state_2_char(zip_code,buyer_data_list)
		else:
			if len(buyer_data_list[7]) > 5:
				zip_code = buyer_data_list[7][:5]
			else:
				zip_code = buyer_data_list[7]
			buyer_data_list[6] = self.update_state_2_char(zip_code,buyer_data_list)

		if len(buyer_data_list) == 11:
			buyer_new_phone_number = re.sub('[\(\)\+\-\ ]', '', str(buyer_data_list[2]))
			phone_number = re.sub('[\(\)\+\-\ ]', '', str(buyer_data_list[10]))
			buyer_data_list[2] = buyer_new_phone_number
			buyer_data_list[10] = phone_number
			add_customer = ("INSERT INTO Customer " "(BuyerEmailAddress,BuyerName,BuyerPhoneNumber,Name,AddressFieldOne,AddressFieldTwo,City,StateOrRegion,PostalCode,CountryCode,PhoneNumber) " "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
		else:
			buyer_new_phone_number = re.sub('[\(\)\+\-\ ]', '', str(buyer_data_list[2]))
			phone_number = re.sub('[\(\)\+\-\ ]', '', str(buyer_data_list[9]))
			buyer_data_list[2] = buyer_new_phone_number
			buyer_data_list[9] = phone_number
			add_customer = ("INSERT INTO Customer " "(BuyerEmailAddress,BuyerName,BuyerPhoneNumber,Name,AddressFieldOne,City,StateOrRegion,PostalCode,CountryCode,PhoneNumber) " "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
		tuple_of_customer = tuple(buyer_data_list)
		try:
			tuple_of_search_customer = tuple(buyer_data_list[:3])
			temp_search = "SELECT * FROM Customer WHERE BuyerEmailAddress = %s AND BuyerName = %s AND BuyerPhoneNumber = %s limit 1"
			cursor.execute(temp_search, tuple_of_search_customer)
			if cursor.fetchone()[0]:
				print "Customer Already Exists"
				cursor.close()
				cnx.close()

		except:
			try:
				cursor.execute(add_customer, tuple_of_customer)
				cnx.commit()
				cursor.close()
				cnx.close()
			except:
				print "Couldnt add customer information"
				cursor.close()
				cnx.close()

	def commit_to_DB(self,list_for_db):
		index_list = [23,25,27,29,31,35,37,41,43,47,51,53,55]
		for index in index_list:
			if list_for_db[index] == '':
				list_for_db[index] = 0.00
			list_for_db[index] = Decimal(list_for_db[index])
		tuple_of_order = tuple(list_for_db)
		try:
			cnx = mysql.connector.connect(user='%s' %(self.dbuser),
										  host='%s' %(self.dbhost),
										  database='%s' %(self.database),
										  password='%s' %(self.dbpassword))
			cursor = cnx.cursor()
		except:
			print "Unable to connect to DB in function commit_to_db"
			exit(4)


		add_amazon_order = ("INSERT INTO Amazon_Order_Report " "(AmazonOrderID,AmazonSessionID,OrderDate,OrderPostedDate,BuyerEmailAddress,BuyerName,BuyerPhoneNumber,FulfillmentMethod,FulfillmentServiceLevel,Name,AddressFieldOne,AddressFieldTwo,City,StateOrRegion,PostalCode,CountryCode,PhoneNumber,AmazonOrderItemCode,SKU,Title,Quantity,ProductTaxCode,ItemType,ItemAmount,ShippingType,ShippingAmount,ItemTaxType,ItemTaxAmount,ShippingTaxType,ShippingTaxAmount,ItemFeeType,ItemFeeAmount,PromotionClaimCode,MerchantPromotionID,PromotionType,PromotionAmount,PromotionShippingType,PromotionShippingAmount,Promotion2ClaimCode,MerchantPromotionID2,Promotion2Type,Promotion2Amount,Promotion2ShippingType,Promotion2ShippingAmount,Promotion3ClaimCode,MerchantPromotionID3,Promotion3Type,Promotion3Amount,Promotion3ShippingType,Promotion3ShippingAmount,Promotion4ClaimCode,MerchantPromotionID4,Promotion4Type,Promotion4Amount,Promotion4ShippingType,Promotion4ShippingAmount,EarliestShipDate,LatestShipDate,EarliestDeliveryDate,LatestDeliveryDate) " "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

		try:
			cursor.execute(add_amazon_order, tuple_of_order)
			cnx.commit()
			cursor.close()
			cnx.close()
		except:
			print "Duplicate Amazon Order"
			cursor.close()
			cnx.close()
			pass


	def send_email(self,failed_message,buyer_data_list):
		to = 'mathewusher@gmail.com'
		gmail_user = 'amazonordercheck@gmail.com'
		gmail_pwd = 'Jakewas6'
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(gmail_user,gmail_pwd)
		header = 'To:' + to + '\n' + 'From:' + gmail_user + '\n' + 'Subject:Check Amazon Order \n'
		msg = header + '\n' + failed_message + '\t' + buyer_data_list[:3]
		smtpserver.sendmail(gmail_user, to, msg)
		smtpserver.close()
