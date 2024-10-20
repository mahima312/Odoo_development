{
    'name': 'CRM Lead KSC',
    'version': '16.1.1',
    'summary': 'Custom CRM Lead Module',
    'description': 'Module to manage leads with custom fields and views.',
    'author': 'Inno-age',
    'category': 'Sales',
    'depends': ['crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
}
