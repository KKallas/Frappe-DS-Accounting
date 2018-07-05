# -*- coding: utf-8 -*-
# Copyright (c) 2018, digitalsputnik and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import re
from frappe.model.document import Document

class Item(Document):
	def autoname(self):
		self.name = "["+self.code+"] "+self.item

	def on_update(self):
		#if self name [*] =! code rename the document
		#find if the name has serial nr in the square brq
		oldName = re.search("\[(.*)\]",self.name)

		if oldName:
			if oldName.group(1) != self.code:
				frappe.rename_doc(self.doctype,self.name,"["+self.code+"] "+self.item)


	def addSource(self,source):
		#FIX THIS if source is marked "1" in the tabe it means OEE
		if source == "1":
			source = "OEE"
		#find is source is in sources list, ignore if allready exists
		for src in self.sources:
			if source in src.source:
				return
		#add source
		new_line = self.append("sources",{"source":source})
		new_line.save()
