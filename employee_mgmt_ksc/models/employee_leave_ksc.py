from odoo import models, fields

class EmployeeLeaveKSC(models.Model):
    _name = 'employee.leave.ksc'
    _description = 'Employee Leave'
    
    employee_id = fields.Many2one(comodel_name='employee.ksc1', string='Employee')
    department_id = fields.Many2one(comodel_name='employee.department.ksc', string='Department')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([('draft', 'Draft'),('approved', 'Approved'), ('refused', 'Refused'),  ('cancelled', 'Cancelled') ], default='draft', string='Status')
    leave_description = fields.Char(string='Leave Description', required=True)
