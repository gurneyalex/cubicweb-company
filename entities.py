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
    

class Company(Division):
    """customized class for Company entities"""
    id = 'Company'

    def parent(self):
        parents = self.is_part_of
        if parents:
            return parents[0]

