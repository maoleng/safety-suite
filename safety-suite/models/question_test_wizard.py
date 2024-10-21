from odoo import models, fields, api


class QuestionTestWizard(models.TransientModel):
    _name = 'thes.question_test_wizard'
    _description = 'Question Test Wizard'

    wizard_id = fields.Many2one('thes.test_wizard', string='Wizard', required=True)
    question_id = fields.Many2one('thes.question', string='Question', required=True)
    content = fields.Text(string='Question Content', related='question_id.content', readonly=True)

    # Related fields to show all possible answers
    answer_a = fields.Char(string='Answer A', related='question_id.answer_a', readonly=True)
    answer_b = fields.Char(string='Answer B', related='question_id.answer_b', readonly=True)
    answer_c = fields.Char(string='Answer C', related='question_id.answer_c', readonly=True)
    answer_d = fields.Char(string='Answer D', related='question_id.answer_d', readonly=True)

    is_multiple_choice = fields.Boolean(string='Is Multiple Choice', related='question_id.is_multiple_choice', readonly=True)


    # User's selected answer
    user_answer = fields.Selection([
        ('A', 'Answer A'),
        ('B', 'Answer B'),
        ('C', 'Answer C'),
        ('D', 'Answer D')
    ], string='Your Answer')

    user_answer_text = fields.Text(string='Your Answer (Fill in the Blank)')
