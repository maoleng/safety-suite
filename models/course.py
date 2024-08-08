from odoo import models, fields

class Course(models.Model):
    _name = 'thes.course'
    _description = 'Course'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    src = fields.Char(string='Source')  # Assuming src is a URL or similar
