from analyzer import Analyzer
from sample_queries import queries

a=Analyzer()
sample=queries[-1]
res=a.analyze(sample)
print(res.pretty())

sample="Clearly incorrect query"
if not a.check(sample):
    print("Indeed")