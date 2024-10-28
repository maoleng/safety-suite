from odoo import models, fields

class QuestionTest(models.Model):
    _name = 'thes.question_test'
    _description = 'Question Test'

    question_id = fields.Many2one('thes.question', string='Question', required=True)
    test_id = fields.Many2one('thes.test', string='Test', required=True, ondelete='cascade')
    user_answer = fields.Selection([
        ('A', 'Answer A'),
        ('B', 'Answer B'),
        ('C', 'Answer C'),
        ('D', 'Answer D')
    ], string='User Answer')
    user_answer_text = fields.Char(string='User Answer (Text)', help="User's answer for fill-in-the-blank questions.")

    content = fields.Text(related='question_id.content', string='Question Content')
    is_multiple_choice = fields.Boolean(string='Is Multiple Choice', related='question_id.is_multiple_choice')
