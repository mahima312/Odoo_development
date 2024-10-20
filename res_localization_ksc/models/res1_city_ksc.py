from odoo import models, fields

class ResCityKSC(models.Model):
    _name = 'res1.city.ksc'
    _description = 'City KSC'

    name = fields.Char(string='City Name', required=True)
    state_id = fields.Many2one('res1.state.ksc', string='State')
