from odoo import models, fields

class CustomManufacturingDashboard(models.Model):
    _name = 'custom_manufacturing.dashboard'
    _description = 'Custom Manufacturing Dashboard'

    # Define your fields here
    production_order_id = fields.Many2one('mrp.production', string='Production Order')
    quantity = fields.Float(string='Quantity')
    product_id = fields.Many2one('product.product', string='Product')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    amount_total = fields.Monetary(string='Total Amount')

