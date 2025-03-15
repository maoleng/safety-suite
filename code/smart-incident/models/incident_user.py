from odoo import models, fields

class IncidentUser(models.Model):
    _name = 'thes.incident_user'
    _description = 'Incident User Assignment'

    incident_id = fields.Many2one('thes.incident', string="Incident", required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string="User", required=True)
