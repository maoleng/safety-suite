from odoo import models, fields, api
from ..external.langchain_utils import extract_incident_details

class Incident(models.Model):
    _name = 'thes.incident'
    _description = 'Incident Reports'

    description = fields.Text(string="Incident Description", required=True)
    type_id = fields.Many2one('thes.type', string="Incident Type")
    location = fields.Char(string="Location")
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Severity")
    corrective_action = fields.Text(string="Corrective Action")

    assigned_users = fields.One2many('thes.incident_user', 'incident_id', string="Assigned Users")


    @api.model
    def create(self, vals):
        """
        Override the create method to automatically extract and save the incident details
        after the description is provided. If the incident type doesn't exist, create a new one.
        """
        description = vals.get('description')

        print(description)
        if description:
            # Extract the details using the external function
            incident_type, location, severity, corrective_action = extract_incident_details(description, self.search([]))

            # Check if the extracted incident type exists in the database
            print(incident_type, location, severity, corrective_action)
            type_record = self.env['thes.type'].search([('name', '=', incident_type)], limit=1)


            if not type_record:
                type_record = self.env['thes.type'].create({'name': incident_type})

            # Set the fields in vals
            vals['type_id'] = type_record.id
            vals['location'] = location
            vals['severity'] = severity.lower()
            vals['corrective_action'] = corrective_action

        # Proceed with the creation of the incident record
        return super(Incident, self).create(vals)