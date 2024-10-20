{
    'name' : 'Hospital Management System',
    'author' : 'Mahima',
    'website' : 'www.odoo.com',
    'summary' : 'Odoo 16 Development',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
    ],
    'data' : [
        'security/ir.model.access.csv',
        # 'views/menu.xml',
        'views/patient.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
    ]

}