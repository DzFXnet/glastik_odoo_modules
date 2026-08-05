from odoo import models, fields

class DzfxTask(models.Model):
    _name = 'dzfx.task'
    _description = 'Dzfx Ieraksts'

    name = fields.Char(string='Nosaukums')
