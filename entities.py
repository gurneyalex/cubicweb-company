"""this contains the template-specific entities' classes

:organization: Logilab
:copyright: 2003-2007 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"

from cubicweb.entities import AnyEntity, fetch_config
 


class Division(AnyEntity):
    """customized class for Division entities"""
    id = 'Division'
    fetch_attrs, fetch_order = fetch_config(['name'])
    
    __rtags__ = {'phone': 'inlineview',
                 'headquarters': 'inlineview',
                 'use_email': 'inlineview'}

class Company(Division):
    """customized class for Company entities"""
    id = 'Company'

    __rtags__ = {
        ('subsidiary_of', 'Company', 'object') : 'create',
        'is_part_of' : 'create',
        }
