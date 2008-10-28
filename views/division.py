"""specific views for division

:organization: Logilab
:copyright: 2003-2007 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
:contact: http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""
__docformat__ = "restructuredtext en"


from company import CompanyBasePrimaryView

class DivisionPrimaryView(CompanyBasePrimaryView):
    id = 'primary'
    accepts = ('Division',)

    PRIMARY_TEMPLATE = """<table border="0" width="100%%">
    <tr>
    <td style="width: 75%%;" valign="top">
    <div class="mainInfo">
    %s
    </div>
    </td>
    </tr>
    </table>
    """

    def cell_call(self, row, col, **kwargs):
        entity = self.complete_entity(row, col)
        self.w(self.PRIMARY_TEMPLATE % self._primary_main_info(entity) )

    def _primary_main_info(self, entity):
        """ Main Block in primary view """
        parent_rql = "Any S, N where D eid %s, S is Company, " \
                     "D is_part_of S, S name N" % entity.eid
        return super(DivisionPrimaryView, self). _primary_main_info(entity, parent_rql)

  

