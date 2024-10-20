from odoo import api, fields, models

class ResCityKsc(models.Model):
    _name = "res.city.ksc"
    _description = "Res City Ksc"

    name = fields.Char(string='City Name', required=True, tracking=True)
    state_name = fields.Char(string='State Name', required=True, tracking=True)
    active = fields.Boolean(string="Active", tracking=True)
    

