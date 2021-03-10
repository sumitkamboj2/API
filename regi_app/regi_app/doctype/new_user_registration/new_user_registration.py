# -*- coding: utf-8 -*-
# Copyright (c) 2021, Sumit and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NewUserRegistration(Document):
	def on_submit(doc):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",doc.email)
		user_doc = frappe.new_doc('User')
		user_doc.email = doc.email
		user_doc.first_name = doc.first_name
		user_doc.enabled = 0 
		user_doc.save(ignore_permissions=True)
		
		frappe.sendmail(
			recipients = doc.email,
			subject = "User Registration Process successfully completed",
			message = "user Registration successfully. used user Id for Login :<br> User Id : {0} ".format(doc.email)
			)