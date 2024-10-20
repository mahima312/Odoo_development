from odoo import models, fields
from odoo.exceptions import UserError

class EmployeeKsc(models.Model):
    _name = 'employee.ksc1'
    _description = 'Employee'
    
    name = fields.Char(string='Name of the employee', required=True)
    department_id = fields.Many2one(comodel_name='employee.department.ksc', string='Department Name', required=True)
    shift_id = fields.Many2one(comodel_name='employee.department.shift.ksc', string='Shift', required=True )
    job_position = fields.Char(string='Job Position of employee')
    salary = fields.Float(string='Salary', digits=(6, 2))
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([ ('male', 'Male'),('female', 'Female'),('transgender', 'Transgender')], string='Gender')
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad_hoc', 'Ad Hoc')], string='Job Type')
    is_manager = fields.Boolean(string='Is Manager')
    manager_id = fields.Many2one(comodel_name='employee.ksc1', string='Manager', ondelete='set null', domain="[('is_manager', '=', True)]", context={'no_create': True, 'no_open': True})
    related_user_id = fields.Many2one(comodel_name='res.users', string='Related User')
    employee_ids = fields.One2many('employee.ksc1', 'manager_id', string='Subordinates', readonly=True)
    increment_percentage = fields.Float(string='Increment Percentage', digits=(2, 2), groups='employee.group_employee')
    
    # def create(self, vals):
    #  if not vals.get('shift_id'):
    #     raise ValidationError('Shift ID must be provided.')
    #  return super(EmployeeKsc, self).create(vals)
