from analyzer import Analyzer
from recreator import Recreator
from sample_queries import queries

# пример использования анализатора для проверки валидности запроса
a = Analyzer()

sample = 'create tabl test_table'
if not a.check(sample):
    print(f'"{sample}" - некорректный запрос')

print()

sample = 'CREATE TABLE test_table;'
if a.check(sample):
    print(f'"{sample}" - корректный запрос')

print()

# пример использования анализатора для построения синтаксического дерева запроса

sample = '''CReatE DATABASE IF NOT EXISTS 
db_name comment 'sample comment' location 'path/to/the/file.db'
with dbproperties(prop1=val1,prop2=val2);'''
res = a.analyze(sample)
print('Синтаксическое дерево запроса:\n',res.pretty())

# пример использования рекреатора для рефакторинга запроса

r = Recreator(res)
print('До рефакторинга:\n',sample,'\n')
print('После рефакторинга:\n',r.recreate())
