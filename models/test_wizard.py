from odoo import models, fields, api

class TestWizard(models.TransientModel):
    _name = 'thes.test_wizard'
    _description = 'Test Wizard'

    test_id = fields.Many2one('thes.test', string='Test', required=True)
    question_test_ids = fields.One2many('thes.question_test_wizard', 'wizard_id', string='Questions')

    @api.model
    def default_get(self, fields):
        res = super(TestWizard, self).default_get(fields)
        test_id = self.env.context.get('active_id')  # Get the test from context
        if test_id:
            res['test_id'] = test_id
            # Pre-load questions from the test into the wizard
            test = self.env['thes.test'].browse(test_id)
            question_tests = []
            for question in test.question_ids:
                question_tests.append((0, 0, {
                    'question_id': question.question_id.id,
                    'content': question.content,
                }))
            res['question_test_ids'] = question_tests
        return res

    def submit_test(self):
        """Submit the user's answers and calculate the score."""
        test = self.test_id
        total_questions = len(self.question_test_ids)
        correct_answers = 0

        for wizard_question in self.question_test_ids:
            question = wizard_question.question_id
            user_answer = wizard_question.user_answer
            # Check if the user's answer matches the true answer
            if user_answer == question.true_answer:
                correct_answers += 1

            # Update the user's answer in the corresponding question_test record
            test_question = self.env['thes.question_test'].search([
                ('test_id', '=', test.id),
                ('question_id', '=', question.id)
            ])
            test_question.user_answer = user_answer

        # Calculate score as a percentage
        score = (correct_answers / total_questions) * 100
        test.score = score
        test.feedback = f"You answered {correct_answers} out of {total_questions} correctly."
        test.attempted_at = fields.Datetime.now()

        # Close the wizard
        return {'type': 'ir.actions.act_window_close'}
