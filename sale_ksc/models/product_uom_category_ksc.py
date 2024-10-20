from odoo import models, fields

class ProductUOMCategoryKSC(models.Model):
    _name = 'product.uom.category.ksc'
    _description = 'Product UOM Category'

    name = fields.Char(string='Name of Product Category', required=True)
    uom_ids = fields.One2many('product.uom.ksc', 'uom_category_id', string='UOMs')
