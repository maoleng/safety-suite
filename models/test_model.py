from odoo import models, fields, api
import random
from ..external.langchain_utils import generate_questions  # Import the external functions

class Test(models.Model):
    _name = 'thes.test'
    _description = 'Test'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    score = fields.Float(string='Score')
    user_id = fields.Many2one('res.users', string='User')
    is_public = fields.Boolean(string='Is Public')
    feedback = fields.Text(string='Feedback')
    attempted_at = fields.Datetime(string='Attempted At')
    finished_at = fields.Datetime(string='Finished At')
    available_at = fields.Datetime(string='Available At')
    expired_at = fields.Datetime(string='Expired At')

    question_ids = fields.One2many('thes.question_test', 'test_id', string='Questions')

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
