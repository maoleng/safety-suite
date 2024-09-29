from odoo import models, fields

class Question(models.Model):
    _name = 'thes.question'
    _description = 'Question'

    content = fields.Text(string='Content', required=True)
    answer_a = fields.Char(string='Answer A', required=True)
    answer_b = fields.Char(string='Answer B', required=True)
    answer_c = fields.Char(string='Answer C', required=True)
    answer_d = fields.Char(string='Answer D', required=True)
    true_answer = fields.Selection([
        ('A', 'Answer A'),
        ('B', 'Answer B'),
        ('C', 'Answer C'),
        ('D', 'Answer D')
    ], string='True Answer', required=True)
