from odoo import models, fields

class DzfxPartner(models.Model):
    _name = "dzfx.partner"
    _description = "DzFX Partner - Contact persons, sub-contractors, clients, etc."

    name = fields.Char(string="Name")
