# -*- coding: utf-8 -*-
{
    'name': "Smart Incident",

    'summary': """
        Optimizing Labor Protection through a Tailored L&D ERP Module on Odoo""",
    'description': """
        The Incident Diagnose and Reporting Module streamlines the process of reporting, analyzing, and addressing workplace incidents using AI. It enables staff to submit reports while AI automatically extracts the incident type, location, and severity. Admins can refine reports, reclassify incidents, and assign corrective actions, with AI providing suggestions based on historical data to ensure efficient and consistent safety management.
    """,
    'icon': '/smart-incident/static/description/icon.png',

    'author': "Bui Huu Loc",
    'website': "https://github.com/maoleng",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/user_management_views.xml',
        'views/user_management_menu.xml',
        'views/incident_management_views.xml',
        'views/incident_management_menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
