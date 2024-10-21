from odoo import models, fields

class Question(models.Model):
    _name = 'thes.question'
    _description = 'Question'

    content = fields.Text(string='Content', required=True)
    is_multiple_choice = fields.Boolean(string='Is Multiple Choice')
    answer_a = fields.Char(string='Answer A')
    answer_b = fields.Char(string='Answer B')
    answer_c = fields.Char(string='Answer C')
    answer_d = fields.Char(string='Answer D')
    true_answer = fields.Selection([
        ('A', 'Answer A'),
        ('B', 'Answer B'),
        ('C', 'Answer C'),
        ('D', 'Answer D')
    ], string='True Answer')
    true_answer_text = fields.Char(string='True Answer (Text)', help="Correct answer for fill-in-the-blank questions.")
