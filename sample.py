from analyzer import Analyzer

a=Analyzer('test_grammar.lark')
sample='''SELECT City FROM Customers
UNION
SELECT City1 FROM Suppliers
UNION ALL
SELECT City2 FROM Suppliers
UNION ALL
SELECT City3 FROM Suppliers
GROUP BY City4;'''
res=a.analyze(sample)
print(res.pretty())