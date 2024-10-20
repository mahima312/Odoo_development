from odoo import models, fields

class CrmLeadKsc(models.Model):
    _inherit = 'crm.lead'

    customer_name = fields.Char(string="Customer Name",required=True)
    customer_email = fields.Char(string="Customer Email",required=True)
    customer_phone = fields.Char( string="Customer Phone",required=True)
    expected_revenue = fields.Float(digits=(16, 3), string="Expected Revenue")
    salesperson = fields.Char(string="Salesperson",required=True,)
    state_sales_team = fields.Char(string="Sales Team")
    campaign = fields.Char(string="Campaign")
    channel = fields.Selection([('facebook', 'Facebook'),('whatsapp', 'WhatsApp'),('email', 'Email'),('newspaper', 'Newspaper'),('television', 'Television'),('phone_call', 'Phone Call'),('sms', 'SMS'),
      ('google_ads', 'Google Ads')], required=True, string="Channel")
    state = fields.Selection([('new', 'New'),('qualified', 'Qualified'),('proposition', 'Proposition'),('won', 'Won'),('lost', 'Lost')], string="State", required=True, default='new')
    next_follow_up_date = fields.Date(string="Next Follow Up Date",required=True)
    won_date = fields.Date(string="Won Date")
    lost_reason = fields.Text(string="Lost Reason")

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'won':
            self.won_date = fields.Date.today()
        elif self.state == 'lost':
            self.lost_reason = 'Reason for losing the lead'
