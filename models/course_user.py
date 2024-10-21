from odoo import models, fields

class CourseUser(models.Model):
    _name = 'thes.course_user'
    _description = 'Course User'

    course_id = fields.Many2one('thes.course', string='Course', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    assigned_at = fields.Datetime(string='Assigned At')
    completed_at = fields.Datetime(string='Completed At')
