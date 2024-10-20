from odoo import models, fields

class ResStateKSC(models.Model):
    _name = 'res.state.ksc'
    _description = 'State'

    name = fields.Char(string='Name of the State', required=True)
    short_code = fields.Char(string='Short Code of the State', required=True)
    country_name = fields.Char(string='Country Name', required=True, copy=False)
    active = fields.Boolean(string='Active', default=True)

    _sql_constraints = [ ('short_code_unique', 'unique(short_code)', 'The short code must be unique!')]

