from odoo import models, fields

class SaleOrderLineKSC(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('sale.order.ksc', string='Order Reference')
    product_id = fields.Many2one('product.ksc1', string='Product')
    name = fields.Text(string='Description')
    quantity = fields.Float(string='Quantity',digits=(6, 2))
    unit_price = fields.Float(string='Unit Price', digits=(6, 2))
    state = fields.Selection([('draft', 'Draft'),('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'),], string='State', default='draft')
    uom_id = fields.Many2one('product.uom.ksc', string='UOM')
