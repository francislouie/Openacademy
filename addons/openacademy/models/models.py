# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date, timedelta


class Section(models.Model):
    _name = 'school.section'

    name = fields.Char(string="Name")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    seats = fields.Integer(string="Number of Seats")
    student_ids = fields.Many2many('school.student',
                                  string="Student")
    student_count = fields.Integer(string="Student count", compute='_student_count')
    color = fields.Integer()
    start_date = fields.Date(default=fields.Date.today,
                             string="Start Date")
    duration = fields.Float(help="Duration in days")
    end_date = fields.Date(string="End Date", compute='_get_end_date', inverse='_set_end_date')

    @api.depends('seats', 'student_ids')
    def _student_count(self):
        for r in self:
            if not r.seats:
                r.student_count = 0.0
            else:
                r.student_count = 100.0 * len(r.student_ids) / r.seats

    @api.onchange('seats', 'student_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.student_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees"),
                },
            }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not(r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration,seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not(r.start_date and r.duration):
                continue
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1


class Student(models.Model):
    _name = 'school.student'

    first_name = fields.Char(string="First Name")
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    name = fields.Char(string="Name")
    section_id = fields.Many2one('school.section',
                                 string="Sections")

    @api.model
    def create(self, values):
        first_name = values['first_name'].upper().strip()
        middle_name = values['middle_name'].upper().strip()
        last_name = values['last_name'].upper().strip()

        values['name'] = first_name + ' ' + middle_name + ' ' + last_name
        values['first_name'] = first_name
        values['middle_name'] = middle_name
        values['last_name'] = last_name

        return super(Student, self).create(values)

    @api.multi
    def write(self, values):
        if values.get('first_name'):
            values['first_name'] = values.get('first_name').upper().strip()
        else:
            if self.first_name != False:
                values['first_name'] = self.first_name.upper().strip()

        if values.get('middle_name'):
            values['middle_name'] = values.get('middle_name').upper().strip()
        else:
            if self.first_name != False:
                values['middle_name'] = self.middle_name.upper().strip()

        if values.get('last_name'):
            values['last_name'] = values.get('last_name').upper().strip()
        else:
            if self.last_name != False:
                values['last_name'] = self.last_name.upper().strip()


        if self.first_name != False or self.first_name != False or self.last_name != False:
            values['name'] = values['first_name'].upper().strip() + ' ' + values['middle_name'].upper().strip() + ' ' + values['last_name'].upper().strip()


        return super(Student, self).write(values)
