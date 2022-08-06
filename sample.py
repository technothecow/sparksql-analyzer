from analyzer import Analyzer

a=Analyzer('grammar.lark')
print(a.analyze('SELECT a, b FROM c WHERE a>b;'))