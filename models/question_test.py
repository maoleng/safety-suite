from odoo import models, fields

class QuestionTest(models.Model):
    _name = 'thes.question_test'
    _description = 'Question Test'

    question_id = fields.Many2one('thes.question', string='Question', required=True)
    test_id = fields.Many2one('thes.test', string='Test', required=True)
    order = fields.Integer(string='Order')
    user_answer = fields.Selection([
        ('a', 'Answer A'),
        ('b', 'Answer B'),
        ('c', 'Answer C'),
        ('d', 'Answer D')
    ], string='User Answer')
