"""company related views in company package

:organization: Logilab
:copyright: 2003-2008 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"

from logilab.mtconverter import html_escape

from cubicweb.common.view import EntityView
from cubicweb.web.views.baseviews import SecondaryView, OneLineView, TextView

from cubicweb.web.views.baseviews import PrimaryView


class CompanyBasePrimaryView(PrimaryView):
    ## Specifc views for Companies and Divisions ###############################
    id = None 
    
    PRIMARY_TEMPLATE = """<table border="0" width="100%%">
    <tr>
    <td style="width: 75%%;" valign="top">
    <div class="mainInfo">
    %s
    </div>
    %s
    </td>
    </tr>
    </table>
    """
    def cell_call(self, row, col, **kwargs):
        entity = self.complete_entity(row, col)
        self.w(self.PRIMARY_TEMPLATE % (
            self._primary_main_info(entity),
            self._primary_main_related(entity),
            ))
      
    def _primary_main_info(self, entity, parent_rql=None):
        """ Main Block in primary view """
        html = [u'<h1>%s</h1>' % html_escape(entity.name)]
        if parent_rql:
            parent_rset = self.req.execute(parent_rql)
            html.append(u'<h2>%s</h2>' % (
                ', '.join(e.view('oneline') for e in parent_rset.entities())))
        # Display direct attributes (address, tel, email, etc.)
        html.append(entity.view('address_view', incontext=True))
        rncs = getattr(entity, 'rncs', entity.name)
        if rncs:
            rncs = html_escape(rncs)
        html.append(u'<p><a href="http://www.societe.com/cgibin/liste?nom=%s">'
                     'Recherche sur societe.com</a></p>' % rncs)
        return u'\n'.join(html)


    def _primary_main_related(self, entity):
        """Side column in primary view"""
        _ = self.req._
        etype = entity.e_schema
        baseurl = self.req.relative_path(includeparams=False)


    def _concat_results(self, query, label, vid):
        """Join the result of view 'vid' on each element in the query's rset
        """
        rset = self.req.execute(query)
        html = [self.view(vid, rset, row=i) for i in range(rset.rowcount)]
        return u'<br/>'.join(html)


    def _main_related_div(self, query, label, vid='secondary'):
        """Creates the side box (<div class="mainRelated") based
        on queries
        
        :type query: str
        :param query: the rql query used to compute displayed data

        :type label: str
        :param label: the box label
    
        :rtype: str
        :return: the HTML/CSS code for the side box
        """
        template = u"""<div class="mainRelated">
        <h2>%s</h2>
        %s
        </div>
        """
        res = self._concat_results(query, label, vid)
        if res:
            return template % (label, res)
        return u''


class CompanyAddressView(EntityView):
    id = 'address_view'
    title = _('address view')
    accepts = ('Company', 'Division')
    
    def cell_call(self, row, col, incontext=False):
        """only prints address"""
        entity = self.complete_entity(row, col)
        self.w(u'<div class="vcard">')
        if not incontext:
            self.w(u'<h3><a class="fn org url" href="%s">%s</a></h3>'
                   % (html_escape(entity.absolute_url()), html_escape(entity.name)))
        self.wview('incontext',entity.related('headquarters'), 'null')
        if entity.web :
            url = html_escape(entity.web)
            self.w(u"<a href='%s'>%s</a><br/>" % (url, url))
        self.wview('list', entity.related('phone'),'null')
        self.wview('list', entity.related('use_email'),'null')
        self.w(u'</div>')


class CompanyPrimaryView(CompanyBasePrimaryView):
    id = 'primary'
    accepts = ('Company','Division')

    
    def _primary_main_info(self, entity):
        """ Main Block in primary view """
        parent_rql = "Any S, N ORDERBY N WHERE S1 eid %s, S is Company, " \
                     "S1 subsidiary_of S, S name N" % entity.eid
        return CompanyBasePrimaryView._primary_main_info(self, entity, parent_rql)

    def _primary_main_related(self, entity):
        """ Block under the main one in primary view """
        _ = self.req._
        # Divisions and child companies ?
        rql = 'Any X,N where E eid %s and ((X is Division, X is_part_of E) or (X is Company, X subsidiary_of E)) and X name N ORDERBY N' % entity.eid
        div_rql = 'Any X,N ORDERBY N ASC WHERE X is Division, E eid %s, X is_part_of E, ' \
                  'E is Company, X name N' % entity.eid
        comp_rql = 'Any X,N ORDERBY N ASC WHERE X is Company, E eid %s, X subsidiary_of E, ' \
                   'E is Company, X name N' % entity.eid
        queries = (
            (div_rql, _('Divisions'), 'address_view'),
            (comp_rql, _('Subsidiaries'), 'address_view'),
            )
        return u'\n'.join([self._main_related_div(r,l,v) for r,l,v in queries])



    
    
