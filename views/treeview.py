"""treeviews

:organization: Logilab
:copyright: 2009 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"
_ = unicode

from logilab.mtconverter import xml_escape

from cubicweb.selectors import one_line_rset, implements, match_kwargs
from cubicweb.view import EntityView
from cubicweb.web.views.treeview import TreeViewItemView

class CompanyTree(EntityView):
    id = 'companytree'
    __select__ = one_line_rset() & implements('Company', 'Division')

    def cell_call(self, row, col):
        entity = self.rset.get_entity(row, col)
        root_company = entity.root()
        self.wview('treeview', root_company.as_rset(), subvid='oneline-selectable',
                   onscreen=entity.eid)

class ComponentTreeItemView(TreeViewItemView):
    """keeps track of which branches to open according to current component"""
    __select__ = (TreeViewItemView.__select__ & implements('Company', 'Division'))

    def cell_call(self, row, col, treeid, vid, parentvid='treeview',
                  **morekwargs):
        onscreen = morekwargs.get('onscreen')
        if onscreen:
            self._compute_open_branches(onscreen)
        else:
            self._open_branch_memo = set()
        super(ComponentTreeItemView, self).cell_call(row, col, treeid,
                                                     vid, parentvid,
                                                     **morekwargs)

    def _compute_open_branches(self, comp_eid):
        entity = self.req.execute('Any C WHERE C eid %(c)s',
                                  {'c': comp_eid}, 'c').get_entity(0, 0)
        self._open_branch_memo = set(entity.path())

    def open_state(self, eeid, treeid):
        return eeid in self._open_branch_memo

class OneLineSelectableView(EntityView):
    """custom oneline view used by company / division treeview"""
    id = 'oneline-selectable'
    __select__ = implements('Company', 'Division') & match_kwargs('onscreen')

    def cell_call(self, row, col, onscreen):
        entity = self.rset.get_entity(row, col)
        self.w(u'<a href="%s"' % xml_escape(entity.absolute_url()))
        if entity.eid == onscreen:
            self.w(u' class="selected">')
        else:
            self.w(u'>')
        self.w(u'%s</a>' % xml_escape(entity.dc_title()))