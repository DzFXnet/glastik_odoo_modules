from odoo import models, fields

class DzfxProject(models.Model):
    _name = "dzfx.project"
    _description = "DzFX Project"

    name = fields.Char(string="Project Name")
