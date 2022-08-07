from analyzer import Analyzer
from recreator import Recreator
from sample_queries import queries

a = Analyzer()
sample = '''CReatE DATABASE IF NOT EXISTS 
db_name comment 'sample comment' location 'path/to/the/file.db'
with dbproperties(prop1=val1,prop2=val2);'''
res = a.analyze(sample)
print(res.pretty())

r = Recreator(res)
print(r.recreate())
