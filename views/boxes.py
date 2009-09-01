# -*- coding: utf-8 -*-

from cubicweb.selectors import implements, score_entity
from cubicweb.web.box import EntityBoxTemplate
from cubicweb.web.htmlwidgets import SideBoxWidget, BoxLink

def has_rncs(entity):
    return entity.rncs is not None

class CompanySeeAlso(EntityBoxTemplate):
    id = 'company_seealso_box'
    __select__ = EntityBoxTemplate.__select__ & implements('Company') #& score_entity(has_rncs)
    order = 25

    def cell_call(self, row, col, **kwargs):
        entity = self.entity(row, col)
        rncs = entity.rncs or u''
        box = SideBoxWidget(self.req._('This company on other sites'),
                            'company_sites%i' % entity.eid)
        box.append(BoxLink('http://www.societe.com/cgibin/liste?nom=%s' % rncs, u'Société.com'))
        box.append(BoxLink('http://www.score3.fr/entreprises.shtml?chaine=%s' % rncs, u'Score3.fr'))
        self.w(box.render())
