# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date


class Section(models.Model):
    _name = 'school.section'

    name = fields.Char(string="Name")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    seats = fields.Integer(string="Number of Seats")
    student_ids = fields.Many2one('school.student',
                                  string="Student")
    student_count = fields.Integer(string="Student count")
    color = fields.Integer()
    start_date = fields.Date(default=fields.Date.today,
                             string="Start Date")
    duration = fields.Float(help="Duration in days")
    end_date = fields.Date(string="End Date")

class Student(models.Model):
    _name = 'school.student'

    name = fields.Char(string="Name")
    section_id = fields.Many2one('school.section',
                                 string="Sections")