// Copyright (c) 2020, Indictrans and contributors
// For license information, please see license.txt



frappe.ui.form.on('Registration', {
	refresh: function(frm) {
		console.log("refresh called................................")
		
	},
	email:function(frm){
		var email_id = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
		if (email_id.test(frm.doc.email) == false)
		{
			frm.set_value('email', '')
			frappe.throw('Enter Correct Email.');

		}
	},
	mobile_number:function(frm){
		if(frm.doc.mobile_number.length != 10 && frm.doc.mobile_number != "") {
			frm.set_value('mobile_number',"")
			frappe.throw("Invalid Mobile number.")
			}
	},
	send_emails:function(frm){
		if (frm.doc.status==="Planned"){
			frappe.call({
				method: "meeting.api.send_invitation_emails",
				args:{
					meeting:frm.doc.name
				}
			});
		}
	},
});



