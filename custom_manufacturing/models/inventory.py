from odoo import models, fields, api

class StockInventory(models.Model):
    _name = 'custom_manufacturing.stock_inventory'
    _description = 'Stock Inventory'

    name = fields.Char(string='Inventory Reference', required=True)
    location_id = fields.Many2one('stock.location', string='Location', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    @api.model
    def create(self, vals):
        # Custom logic for creation
        return super(StockInventory, self).create(vals)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_validate(self):
        self.state = 'done'
