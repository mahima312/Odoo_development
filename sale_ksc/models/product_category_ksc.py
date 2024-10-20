from odoo import models, fields

class ProductCategoryKsc(models.Model):
    _name = 'product.category.ksc'
    _description = 'Product Category Ksc'
    
    name = fields.Char(string='Name of Product', required=True)
    parent_id = fields.Many2one('product.category.ksc', string='Parent Category', ondelete='cascade')

    
