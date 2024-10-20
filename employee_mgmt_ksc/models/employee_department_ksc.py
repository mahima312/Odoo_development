from odoo import models, fields

class EmployeeDepartment(models.Model):
    _name = 'employee.department.ksc'
    _description = 'Employee Department'
    
    name = fields.Char(string='Department Name', required=True)
    employee_ids = fields.One2many('employee.ksc1', 'department_id', string='Employees')
    department_manager_id = fields.Many2one(comodel_name='res.users', string='Department Manager')

