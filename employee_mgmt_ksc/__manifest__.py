{
    'name': 'Employee Management KSC',
    'version': '16.1.1',
    'summary': 'Employee Management System',
    'description': """
        A module to manage employees, departments, shifts, and leaves.""",
    'author': 'Inno-Age',
    'depends': ['base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_department_views.xml',
        'views/employee_department_shift_views.xml',
        'views/employee_views1.xml',
        'views/employee_leave_views.xml',
    ],
    'installable': True,
    'application': True,
}
