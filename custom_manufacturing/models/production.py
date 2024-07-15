from odoo import models, fields, api

class ProductionOrder(models.Model):
    _name = 'custom_manufacturing.production_order'
    _description = 'Production Order'

    name = fields.Char(string='Order Reference', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    invoice_id = fields.Many2one('account.move', string='Invoice')

    @api.model
    def create(self, vals):
        # Custom logic for creation
        return super(ProductionOrder, self).create(vals)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_start_production(self):
        self.state = 'in_progress'

    def action_complete_production(self):
        self.state = 'done'
        # Create invoice
        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.sale_order_id.partner_id.id,
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product_id.id,
                'quantity': self.quantity,
                'price_unit': self.product_id.lst_price,
            })],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        self.invoice_id = invoice.id
