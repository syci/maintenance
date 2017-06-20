# -*- coding: utf-8 -*-
# Copyright 2017 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Maintenance Settings',
    'summary': 'Provides general settings for the Maintenance App',
    'author': 'Onestein, Odoo Community Association (OCA)',
    'website': 'http://www.onestein.eu',
    'category': 'Maintenance',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'maintenance',
    ],
    'data': [
        'data/maintenance_data.xml',
        'security/maintenance_security.xml',
        'views/maintenance_config_settings.xml',
        'menuitems.xml',
    ],
}
