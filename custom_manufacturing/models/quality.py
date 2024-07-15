from odoo import models, fields, api

class QualityCheck(models.Model):
    _name = 'custom_manufacturing.quality_check'
    _description = 'Quality Check'

    name = fields.Char(string='Check Reference', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    result = fields.Selection([
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ], string='Result')
