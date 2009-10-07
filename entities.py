"""this contains the template-specific entities' classes

:organization: Logilab
:copyright: 2003-2007 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"

from cubicweb.entities import AnyEntity, fetch_config
from cubicweb.common.mixins import TreeMixIn
from cubicweb.interfaces import ITree

class Division(TreeMixIn, AnyEntity):
    """customized class for Division entities"""
    id = 'Division'
    __implements__ = AnyEntity.__implements__ + (ITree,)
    fetch_attrs, fetch_order = fetch_config(['name'])
    tree_attribute = 'is_part_of'

class Company(Division):
    """customized class for Company entities"""
    id = 'Company'
    __implements__ = AnyEntity.__implements__ + (ITree,)
    tree_attribute = 'subsidiary_of'
