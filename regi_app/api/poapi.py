
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import json
@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

@frappe.whitelist(allow_guest=True)
def create_po(data):
	if data:
		try:
			data = json.loads(data)
			po_doc = frappe.new_doc("Purchase Order")
			po_doc.supplier = data.get("supplier")
			po_doc.transaction_date = data.get("transaction_date")
			po_doc.schedule_date = data.get("schedule_date")
			for item_data in data["items"]:
				po_doc.append(
					"items", 
					{
						"item_code":item_data.get("item_code"),
						"item_name":item_data.get("item_name"),
						"qty":item_data.get("qty"),
						"rate":item_data.get("rate")
					})

			po_doc.save(ignore_permissions=True);
			frappe.db.commit();
			return "Purchase Order Successfully created."
		except Exception as e:
			raise e
		

	