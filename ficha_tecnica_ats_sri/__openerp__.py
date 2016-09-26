# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Anexo Transacional Simplificado',
    'version': '1.331',
    'category': 'Localization/Account Charts',
    'description': """
Ficha Técnica del ATS-SRI Soporte MULTIUSUARIO - ESTE MODULO ESTA DESARROLLADO BAJO LICENCIA DE SOFTWARE LIBRE LGPLv3.
==============================================================================

Módulo gratuito, desarrollado por la comunidad de software libre de odoo-group-ecuador incluye:
-Campos para importar facturas electrónicas de Ecuador
-Ficha Técnica ATS de Agosto de 2016
-Métodos de Pago (Incluído Dinero Electrónico
-Formato Genérico Simple de Impresión de Factura PDF-Qweb
-Numeración automática de documentos con secuencial y autorización
-Full Integración Nativa con Odoo
y mucho más...

Este módulo es Gratuito y esta disponible para cualquier optimización
compártalo con sus amigos y contribuya con este proyecto.

    """,
    'author': 'odoo-group-ecuador',
    'depends': ['account',
                "base_vat",
    ],
    'data': [
        'tablas_model/views/tablas_view.xml',
        'tablas_model/data/tipo.sustento.csv',
        'tablas_model/data/tipo.comprobante.csv',
        'tablas_model/data/tipo.transaccion.csv',
        'tablas_model/data/identificacion.referencial.csv',
        'tablas_model/data/codigo.retencion.csv',
        'tablas_model/data/tipo.identificacion.csv',
        'tablas_model/data/forma.pago.csv',
        'pestana_sri/pestana_sri_view.xml',
        'search_by_x_identificacion/res_partner_view.xml',
        'account_invoice/views/factura_retencion_view.xml',
        'account_tax/views/account_tax_view.xml',
        'security/ir.model.access.csv',
        'account_invoice/views/factura_report.xml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'website': 'https://www.odoo.com',
}

