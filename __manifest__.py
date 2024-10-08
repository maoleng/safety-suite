# -*- coding: utf-8 -*-
{
    'name': "Safety Suite",

    'summary': """
        Optimizing Labor Protection through a Tailored L&D ERP Module on Odoo""",
    'description': """
        The labor protection industry demands rigorous training and continuous skill enhancement to ensure safety and compliance with regulations. Traditional training methods often fall short in providing efficient management and assessment of employee training. This thesis addresses these challenges by developing an ERP module within Odoo that streamlines the entire process, from onboarding to training completion.
    """,
    'icon': '/safety-suite/static/description/icon.png',

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
        'views/course_management_views.xml',
        'views/course_management_menu.xml',
        'views/test_management_views.xml',
        'views/test_management_menu.xml',
        'views/test_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
