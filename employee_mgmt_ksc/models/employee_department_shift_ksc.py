from odoo import models, fields

class EmployeeDepartmentShift(models.Model):
    _name = 'employee.department.shift.ksc'
    _description = 'Employee Department Shift'
    _rec_name = 'shift'
    
    shift = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon'),('evening', 'Evening'),('night', 'Night') ], string='Shift')
    employee_ids = fields.One2many(comodel_name='employee.ksc1', inverse_name='shift_id', string='Employees', required=True)
