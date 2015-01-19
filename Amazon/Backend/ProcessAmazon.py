#!/usr/bin/python2.7

from NewAmazonGetOrders import NewAmazonGetOrders
from ProcessDBtoSBC import ProcessDBtoSBC
from ProcessSBCtoDB import ProcessSBCtoDB
from ProcessDBtoAmazon import ProcessDBtoAmazon

#This works
#NewOrder = NewAmazonGetOrders('173.9.236.179', 'matt', 'PLOK1234plok')
#NewOrder.main_logic()

# For Testing
#NewOrder.Amazonftpget()
#NewOrder.Add_xml_to_list()
#NewOrder.AmazonXML()

#This works
#Newsearch = ProcessDBtoSBC('173.9.236.179', 'matt', 'PLOK1234plok')
#Newsearch.main_logic()

# For testing
#Newsearch.search_for_orders_not_processed()
#Newsearch.search_for_mfg_information("APE","amazon")
#Newsearch.search_orders_by_customer()\

# This works
SBCtoDB = ProcessSBCtoDB('173.9.236.179', 'matt', 'PLOK1234plok')
SBCtoDB.main_logic()


# This works
#DBtoAmazon = ProcessDBtoAmazon('173.9.236.179', 'matt', 'PLOK1234plok')
#DBtoAmazon.main_logic()


