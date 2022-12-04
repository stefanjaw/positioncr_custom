# -*- coding: utf-8 -*-
# from odoo import http


# class PositioncrCustom(http.Controller):
#     @http.route('/positioncr_custom/positioncr_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/positioncr_custom/positioncr_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('positioncr_custom.listing', {
#             'root': '/positioncr_custom/positioncr_custom',
#             'objects': http.request.env['positioncr_custom.positioncr_custom'].search([]),
#         })

#     @http.route('/positioncr_custom/positioncr_custom/objects/<model("positioncr_custom.positioncr_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('positioncr_custom.object', {
#             'object': obj
#         })
