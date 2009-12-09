"""company related views in company package

:organization: Logilab
:copyright: 2003-2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"

from logilab.mtconverter import xml_escape

from cubicweb.view import EntityView
from cubicweb.selectors import implements
from cubicweb.web import uicfg
from cubicweb.web.views import primary

uicfg.actionbox_appearsin_addmenu.tag_object_of(('*', 'subsidiary_of', 'Company'), True)
uicfg.actionbox_appearsin_addmenu.tag_object_of(('*', 'is_part_of', 'Company'), True)
uicfg.actionbox_appearsin_addmenu.tag_subject_of(('Company', 'is_part_of', '*'), True)

uicfg.autoform_section.tag_subject_of(('*', 'phone', '*'), 'inlined', 'attributes')
uicfg.autoform_section.tag_subject_of(('*', 'headquarters', '*'), 'inlined', 'attributes')

_pvs = uicfg.primaryview_section
_pvs.tag_subject_of(('Company', 'headquarters', 'PostalAddress'), 'hidden')
_pvs.tag_subject_of(('Company', 'phone', '*'), 'hidden')
_pvs.tag_subject_of(('Company', 'use_email', '*'), 'hidden')
_pvs.tag_subject_of(('Company', 'web', '*'), 'hidden')
_pvs.tag_subject_of(('Division', 'headquarters', 'PostalAddress'), 'hidden')
_pvs.tag_subject_of(('Division', 'phone', '*'), 'hidden')
_pvs.tag_subject_of(('Division', 'web', '*'), 'hidden')
_pvs.tag_subject_of(('Division', 'use_email', '*'), 'hidden')
_pvs.tag_subject_of(('*', 'is_part_of', 'Company'), 'relations')
_pvs.tag_object_of(('*', 'is_part_of', 'Company'), 'relations')
_pvs.tag_subject_of(('*', 'subsidiary_of', 'Company'), 'relations')
_pvs.tag_object_of(('*', 'subsidiary_of', 'Company'), 'relations')

class CompanyDivisionPrimaryView(primary.PrimaryView):
    __select__ = implements('Company','Division')

    def render_entity_attributes(self, entity, siderelations=None):
        self.w(entity.view('address_view', incontext=True))


class CompanyAddressView(EntityView):
    __regid__ = 'address_view'
    title = _('address view')
    __select__ = implements('Company', 'Division')

    def cell_call(self, row, col, incontext=False):
        """only prints address"""
        entity = self.cw_rset.complete_entity(row, col)
        self.w(u'<div class="vcard">')
        if not incontext:
            self.w(u'<h3><a class="fn org url" href="%s">%s</a></h3>'
                   % (xml_escape(entity.absolute_url()), xml_escape(entity.name)))
        self.wview('incontext',entity.related('headquarters'), 'null')
        if entity.web :
            url = xml_escape(entity.web)
            self.w(u"<a href='%s'>%s</a><br/>" % (url, url))
        self.wview('list', entity.related('phone'),'null')
        self.wview('list', entity.related('use_email'),'null')
        self.w(u'</div>')


