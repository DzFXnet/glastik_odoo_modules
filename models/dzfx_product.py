from odoo import models, fields

class DzfxProduct(models.Model):
    _name = "dzfx.product"
    _description = "DzFX Product"

    name = fields.Char(string="Product Name")
