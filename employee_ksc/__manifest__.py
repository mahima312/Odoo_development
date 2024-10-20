{
    'name': 'Employee KSC',
    'version': '16.1.1',
    'category': 'Employee',
    'summary': 'Manage Employee Details',
    'author': 'Inno-age',
    'depends': ['base'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}
