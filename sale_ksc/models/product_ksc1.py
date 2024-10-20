from odoo import models, fields

class ProductKSC1(models.Model):
    _name = 'product.ksc1'
    _description = 'Product KSC1'

    name = fields.Char(string='Name of the Product', required=True)
    sku = fields.Char(string='SKU', required=True)
    weight = fields.Float(string='Weight', digits=(6, 2))
    length = fields.Float(string='Length', digits=(6, 2))
    volume = fields.Float(string='Volume', digits=(6, 2))
    width = fields.Float(string='Width', digits=(6, 2))
    barcode = fields.Char(string='Barcode')
    product_type = fields.Selection([('storable', 'Storable'), ('consumable', 'Consumable'), ('service', 'Service')],string='Product Type')
    sale_price = fields.Float(string='Sale Price', digits=(6, 2), default=1.00)
    cost_price = fields.Float(string='Cost Price', digits=(6, 2), default=1.00)
    product_category_id = fields.Many2one('product.category.ksc', string='Product Category')
    uom_id = fields.Many2one('product.uom.ksc', string='UOM')
