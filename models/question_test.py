from odoo import models, fields

class QuestionTest(models.Model):
    _name = 'thes.question_test'
    _description = 'Question Test'

    question_id = fields.Many2one('thes.question', string='Question', required=True)
    test_id = fields.Many2one('thes.test', string='Test', required=True)
    order = fields.Integer(string='Order')
    user_answer = fields.Selection([
        ('A', 'Answer A'),
        ('B', 'Answer B'),
        ('C', 'Answer C'),
        ('D', 'Answer D')
    ], string='User Answer')

    content = fields.Text(related='question_id.content', string='Question Content')
