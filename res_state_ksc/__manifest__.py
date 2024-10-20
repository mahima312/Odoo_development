{
    'name': 'State KSC',
    'version': '16.1.1',
    'summary': 'Manage States',
    'sequence': 10,
    'description': 'Manage states with unique codes and country names.',
    'category': 'Localization',
    'author': 'Inno_Age',
    'depends': ['base', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_state_ksc_views.xml',
        'data/res_state_ksc_data.xml',
    ],
    'installable': True,
    'application': True,
}
