from analyzer import Analyzer
from sample_queries import queries

a=Analyzer()
sample=queries[-1]
res=a.analyze(sample)
print(res.pretty())