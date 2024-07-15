from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    production_order_ids = fields.One2many('custom_manufacturing.production_order', 'sale_order_id', string='Production Orders')
