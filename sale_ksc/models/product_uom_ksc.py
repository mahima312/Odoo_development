class ProductUOMKSC(models.Model):
    _name = 'product.uom.ksc'
    _description = 'Product UOM KSC'

    name = fields.Char()
    uom_category_id = fields.Many2one('product.uom.category.ksc', string='UOM Category')
