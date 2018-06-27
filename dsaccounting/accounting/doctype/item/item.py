# -*- coding: utf-8 -*-
# Copyright (c) 2018, digitalsputnik and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Item(Document):
	def autoname(self):
		self.name = "["+self.code+"] "+self.item

	def addSource(self,source):
		#if source is marked "1" in the tabe it means OEE
		if source == "1":
			source = "OEE"
		#find is source is in sources list, ignore if allready exists
		for src in self.sources:
			if source in src.source:
				return
		#add source
		new_line = self.append("sources",{"source":source})
		new_line.save()
