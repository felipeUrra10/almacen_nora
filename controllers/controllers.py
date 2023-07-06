# -*- coding: utf-8 -*-
# from odoo import http


# class AlmacenNora(http.Controller):
#     @http.route('/almacen_nora/almacen_nora', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/almacen_nora/almacen_nora/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('almacen_nora.listing', {
#             'root': '/almacen_nora/almacen_nora',
#             'objects': http.request.env['almacen_nora.almacen_nora'].search([]),
#         })

#     @http.route('/almacen_nora/almacen_nora/objects/<model("almacen_nora.almacen_nora"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('almacen_nora.object', {
#             'object': obj
#         })
