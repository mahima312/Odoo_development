from odoo import models, fields

class PartnerKSC(models.Model):
    _name = 'res.partner.ksc'
    _description = 'Sale Order'
    

    name = fields.Char(string='Name')
    street1 = fields.Char(string='Street 1')
    street2 = fields.Char(string='Street 2')
    country = fields.Many2one('res.country.ksc',string='Country')
    city = fields.Many2one('res.city.ksc',string='City')
    state = fields.Many2one('res.state.ksc',string='State')
    zip_code = fields.Char(string='Zip Code')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='mobile')
    photo = fields.Image(string='Photo')
    website = fields.Char(string='Website')
    active = fields.Boolean(string ='Active')
    weight = fields.Float(string='Weight')
    address_type = fields.Selection([ ('invoice', 'Invoice'), ('shipping', 'Shipping'), ('contact', 'Contact'), ], string='Address Type')
    parent_id = fields.Many2one('res.partner.ksc', string='Parent Partner', ondelete='cascade')
    child_ids = fields.One2many('res.partner.ksc', 'parent_id', string='Children')
