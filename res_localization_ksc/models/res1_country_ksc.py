from odoo import models, fields

class ResCountryKSC(models.Model):
    _name = 'res1.country.ksc'
    _description = 'Country KSC'

    name = fields.Char(string='Name of the Country', required=True)
    code = fields.Char(string='Short Code of the Country', required=True)
    state_ids = fields.One2many('res1.state.ksc', 'country_id', string='States')
