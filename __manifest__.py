# -*- coding: utf-8 -*-
{
    'name': "Website Date of Birth",

    'summary': """
        Adds date of birth field to partner and website checkout form.
    """,

    'description': """
        Adds date of birth field to partner and website checkout form.
    """,

    'author': "Mint System GmbH",
    'website': "https://www.mint-sytem.ch",
    'category': 'Uncategorized',
    'version': '13.0.0.0.0',

    'depends': ['base', 'website'],

    'data': [
        #'security/ir.model.access.csv',
        'views/view_partner_form.xml',
    ],

    'demo': [
        #'demo/demo.xml',
    ],

    'installable': True,
    'application': False,
}