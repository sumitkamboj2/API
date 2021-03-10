# Copyright (c) 2013, Sumit and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():

	columns = [
		_("Date") + ":Data:120",
		_("Name") + ":Data:150",
		_("Customer") + ":Data:130",
		_("Item code") + ":Float:80",
		_("Quantity") + ":Float:80",
		_("Amount") + ":Float:110",
		_("Grand Total") + ":Float:130",

	]
	return columns

def get_data(filters):
	# query_data = []
	
	query_data = frappe.db.sql("""
		SELECT 
			si.posting_date, si.name,si.customer,sii.item_code,sii.qty,sii.amount,si.grand_total
		FROM 
			`tabSales Invoice` si,
			`tabSales Invoice Item` sii
		WHERE sii.parent = si.name AND si.docstatus = 1 AND {0}	
		""".format(get_conditions(filters)))
	return query_data

def get_conditions(filters):
	cond = '1=1'
	if filters.get('start_date'):
		cond += ' and si.posting_date >= {0}'.format(filters.get('start_date'))
	#if filters.get('end_date'):
	#	cond += ' and si.posting_date <= {0}'.format(filters.get('end_date'))
	return cond	

	