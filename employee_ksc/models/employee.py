from odoo import models, fields

class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee Details'

    name = fields.Char(string='Employee Name', required=True)
    department_name = fields.Char(string='Department Name')
    job_position = fields.Char(string='Job Position')
    salary = fields.Float(string='Salary', digits=(6, 2))
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('transgender', 'Transgender')], string='Gender')
    job_type = fields.Selection([('permanent', 'Permanent'),('ad_hoc', 'Ad Hoc')], string='Job Type')
