# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResPartner(models.Model):
	_inherit = 'res.partner'

	ms_date_of_birth = fields.Date(string='Date of Birth',website_form_blacklisted=False)
