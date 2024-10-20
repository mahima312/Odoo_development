from odoo import models, fields

class ResCountryKsc(models.Model):
    _name = 'res.country.ksc'
    _description = 'Country Ksc'

    name = fields.Char(string='Name of the Country', required=True)
    short_code = fields.Char(string='Short Code of the Country', required=True)
    active = fields.Boolean(string='Active', default=True)
