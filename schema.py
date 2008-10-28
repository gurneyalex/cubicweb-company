from cubicweb.common.schema import format_constraint

# template's specific schema

class Division(EntityType):
    name = String(required=True, fulltextindexed=True, indexed=True, maxsize=64)
    headquarters = SubjectRelation('PostalAddress', cardinality='*?', composite='subject')
    web = String(fulltextindexed=True, maxsize=128)
    phone = SubjectRelation('PhoneNumber', cardinality='*?', composite='subject')
    use_email = SubjectRelation('EmailAddress', cardinality='*+', composite='subject')

class Company(Division):
    rncs = String(fulltextindexed=True, maxsize=32)
    is_part_of = ObjectRelation('Division', cardinality='1*')
    subsidiary_of = SubjectRelation('Company', cardinality='?*')


