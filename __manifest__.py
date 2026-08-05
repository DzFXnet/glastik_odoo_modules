{
    'name': 'Glastik_Inventory',
    'version': '1.0',
    'summary': 'Basic inventory-related entities (tasks, partners, projects, products)',
    'description': 'Inventory tools module for Odoo.',
    'author': 'Dzintars',
    'category': 'Inventory',
    'depends': ['base', 'base_setup'],

    'images': ['static/description/icon.png'],

    'data': [
        'security/ir.model.access.csv',
        'views/dzfx_menu.xml',
        'views/dzfx_task_views.xml',
        'views/dzfx_partner_views.xml',
        'views/dzfx_project_views.xml',
        'views/dzfx_product_views.xml',
    ],

    'installable': True,
    'application': True,
}
