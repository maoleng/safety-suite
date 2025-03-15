from odoo import models, fields

class Type(models.Model):
    _name = 'thes.type'
    _description = 'Type'

    name = fields.Char(string='Name', required=True)
