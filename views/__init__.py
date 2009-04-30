"""template-specific forms/views/actions/components"""
from cubicweb.web import uicfg

uicfg.rmode.tag_relation('create', ('*', 'subsidiary_of', 'Company'), 'object')
uicfg.rmode.tag_relation('create', ('*', 'is_part_of', 'Company'), 'object')
uicfg.rmode.tag_relation('create', ('Company', 'is_part_of', '*'), 'subject')


uicfg.rinlined.tag_relation(True, ('Division', 'phone', '*'), 'subject')
uicfg.rinlined.tag_relation(True, ('Division', 'headquarters', '*'), 'subject')
