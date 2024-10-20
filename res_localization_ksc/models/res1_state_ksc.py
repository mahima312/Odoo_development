from odoo import models, fields

class ResStateKSC(models.Model):
    _name = 'res1.state.ksc'
    _description = 'State KSC'

    name = fields.Char(string='Name of the State', required=True)
    code = fields.Char(string='Short Code of the State', required=True)
    country_id = fields.Many2one('res1.country.ksc', string='Country')
    city_ids = fields.One2many('res1.city.ksc', 'state_id', string='Cities')
