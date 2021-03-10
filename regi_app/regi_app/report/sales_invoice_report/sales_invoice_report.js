frappe.query_reports["Sales Invoice Report"] = {
	"filters": [
	{
		"fieldname":"start_date",
		"label": __("Start Date"),
		"fieldtype": "Date",
		"default": frappe.datetime.get_today(),
		
	},
	{
		"fieldname":"end_date",
		"label": __("End Date"),
		"fieldtype": "Date",
		"default": frappe.datetime.get_today(),
		
	},
    ]
};

