from odoo import models, fields, api
import random
from ..external.langchain_utils import generate_questions  # Import the external functions
from datetime import datetime

class Test(models.Model):
    _name = 'thes.test'
    _description = 'Test'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    score = fields.Float(string='Score')
    user_id = fields.Many2one('res.users', string='User')
    feedback = fields.Text(string='Feedback')
    attempted_at = fields.Datetime(string='Attempted At')
    available_at = fields.Datetime(string='Available At')
    expired_at = fields.Datetime(string='Expired At')

    question_ids = fields.One2many('thes.question_test', 'test_id', string='Questions')

    can_do_test = fields.Boolean(string="Can Do Test", compute="_compute_can_do_test")
    show_questions = fields.Boolean(string='Show Questions', compute='_compute_show_questions')

    def _compute_show_questions(self):
        for record in self:
            admin_group = self.env.ref('base.group_system')
            record.show_questions = self.env.user in admin_group.users

    @api.depends('available_at', 'expired_at', 'attempted_at')
    def _compute_can_do_test(self):
        current_time = datetime.now()
        for test in self:
            # Logic to check if the test can be taken
            if not test.id:
                test.can_do_test = False
            elif not test.attempted_at and test.available_at <= current_time <= test.expired_at:
                test.can_do_test = True
            else:
                test.can_do_test = False

    @api.model
    def create(self, vals):
        # Create the test record
        test = super(Test, self).create(vals)

        # Generate questions using the LangChain utility
        questions = generate_questions()

        # Create and link questions to the test
        for question_data in questions:
            question = self.env['thes.question'].create({
                'content': question_data['content'],
                'answer_a': question_data['answer_a'],
                'answer_b': question_data['answer_b'],
                'answer_c': question_data['answer_c'],
                'answer_d': question_data['answer_d'],
                'true_answer': question_data['true_answer'],
            })

            # Link the question to the test
            self.env['thes.question_test'].create({
                'question_id': question.id,
                'test_id': test.id,
                'order': random.randint(1, 10),
            })

        return test
