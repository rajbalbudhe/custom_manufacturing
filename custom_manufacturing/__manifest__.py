{
    'name': 'Custom Manufacturing',
    'version': '1.0',
    'category': 'Manufacturing',
    'summary': 'Custom module for manufacturing processes',
    'description': """
        This module customizes the manufacturing process by introducing 
        new models and views for production orders, inventory management, 
        quality checks, and more.
    """,
    'author': 'Your Company',
    'website': 'http://www.yourcompany.com',
    'depends': ['base', 'sale', 'stock', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/production_views.xml',
        'views/inventory_views.xml',
        'views/order_views.xml',
        'views/quality_views.xml',
        # 'views/dashboard_views.xml',
        'reports/reports.xml',
        'reports/production_report.xml',
        'reports/inventory_report.xml',
        'reports/sale_report.xml',
        'reports/quality_report.xml',
        'data/email_templates.xml',
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False,
}
