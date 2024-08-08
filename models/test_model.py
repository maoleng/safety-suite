from odoo import models, fields

class Test(models.Model):
    _name = 'thes.test'
    _description = 'Test'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    score = fields.Float(string='Score')
    time = fields.Float(string='Time')  # Assuming time is in minutes or similar
    user_id = fields.Many2one('res.users', string='User')
    is_public = fields.Boolean(string='Is Public')
    feedback = fields.Text(string='Feedback')
    attempted_at = fields.Datetime(string='Attempted At')
    finished_at = fields.Datetime(string='Finished At')
    available_at = fields.Datetime(string='Available At')
    expired_at = fields.Datetime(string='Expired At')

