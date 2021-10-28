from odoo import models, fields

class TestModel(models.Model):
    _name = "placement.portal"
    _description = "A PLacement portal by MissionEd to bring together recruitters and candidates."

    company = fields.Char(string='Company Name',required=True)
    profile = fields.Char(string='Job Profile',required=True)
    ctc = fields.Float(string='CTC (LPA)',required=True)
    openings = fields.Integer(string='Available Openings')
    description = fields.Text(string='Job Description',required=True)