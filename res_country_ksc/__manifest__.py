{
    'name': 'Country Management KSC',
    'version': '16.1.1',
    'summary': 'Manage countries',
    'description': 'This module allows managing countries with custom fields and actions.',
    'author': 'Inno-age',
    'depends': ['base', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_country_ksc_views.xml',
        'data/res_country_ksc_data.xml',
    ],
    'installable': True,
    'application': True,
}
