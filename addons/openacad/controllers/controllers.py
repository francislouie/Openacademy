# -*- coding: utf-8 -*-
from odoo import http

# class Openacad(http.Controller):
#     @http.route('/openacad/openacad/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacad/openacad/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacad.listing', {
#             'root': '/openacad/openacad',
#             'objects': http.request.env['openacad.openacad'].search([]),
#         })

#     @http.route('/openacad/openacad/objects/<model("openacad.openacad"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacad.object', {
#             'object': obj
#         })