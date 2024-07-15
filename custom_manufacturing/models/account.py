from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    production_order_id = fields.Many2one('custom_manufacturing.production_order', string='Production Order')
