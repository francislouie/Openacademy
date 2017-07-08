from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'
    # _rec_name = 'name'
    _description = 'New Partner'

    instructor = fields.Char(string="Instructor")
    section_ids = fields.Many2many('school.section', string="Section")