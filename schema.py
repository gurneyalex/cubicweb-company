from cubicweb.schema import format_constraint

# template's specific schema

class Division(EntityType):
    name = String(required=True, fulltextindexed=True, indexed=True, maxsize=128)
    headquarters = SubjectRelation('PostalAddress', cardinality='*?', composite='subject')
    web = String(fulltextindexed=True, maxsize=128)
    phone = SubjectRelation('PhoneNumber', cardinality='*?', composite='subject')
    use_email = SubjectRelation('EmailAddress', cardinality='*+', composite='subject')
    is_part_of = SubjectRelation('Company', cardinality='1*')

class Company(Division):
    rncs = String(fulltextindexed=True, maxsize=32)
    subsidiary_of = SubjectRelation('Company', cardinality='?*')


