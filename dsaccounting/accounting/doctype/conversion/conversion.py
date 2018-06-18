# -*- coding: utf-8 -*-
# Copyright (c) 2018, digitalsputnik and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from xml.dom import minidom
import urllib2
import datetime
import frappe
from frappe.model.document import Document

class Conversion(Document):
	def updateFromFile(self):
		"""
		The attachment to conversion should be the historical XML from European central bank against EUR
		To be used only for system setup, afterwards have a background jub to pull in daily rates once a day
		"""
		# get attached documents
		# TODO some better filtering than just taking the 1st attachment
		docs = frappe.get_all("File",{"attached_to_doctype":"Conversion","attached_to_name":self.name},['name','file_url'])

		# open the XML from web
		webanswer = urllib2.urlopen(docs[0].file_url)
		xmlfile = webanswer.read()
		xmldoc = minidom.parseString(xmlfile)
		lines = xmldoc.getElementsByTagName('Obs')
		# delete all obsolote data
		self.history = []

		#insert new data
		for dailyrate in lines:
			self.append("history",{"date":datetime.datetime.strptime(dailyrate.getAttribute("TIME_PERIOD"),"%Y-%m-%d"),"rate":dailyrate.getAttribute("OBS_VALUE")})

		#save
		self.save()

	def get_historical(self,date):
		pass



def get_hostoric_currencies(path_to_update_file):
	# get a list off all currencies
	list_of_currencies = frappe.get_all("Conversion")
	# delete all historic data
	for currency in currencies:
		currency.history = []
		currency.save()
	# create new historic data
	xmldoc = minidom.parse(path_to_update_file)
	all_lines = xmldoc.getElementsByTagName('Obs')


	for currency in currencies:
		name = currency.short



def get_today_currencies(path_to_update_file):
	pass
