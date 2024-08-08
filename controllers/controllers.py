# -*- coding: utf-8 -*-
# from odoo import http


# class My-module-1(http.Controller):
#     @http.route('/my-module-1/my-module-1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my-module-1/my-module-1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my-module-1.listing', {
#             'root': '/my-module-1/my-module-1',
#             'objects': http.request.env['my-module-1.my-module-1'].search([]),
#         })

#     @http.route('/my-module-1/my-module-1/objects/<model("my-module-1.my-module-1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my-module-1.object', {
#             'object': obj
#         })
