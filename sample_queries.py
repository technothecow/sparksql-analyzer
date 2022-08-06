queries=[
    '''SELECT *

FROM stars;
''',
    '''SELECT id, name, age

FROM students

WHERE age>=10;''',
    '''SELECT id, name

FROM students;''',
    '''SELECT id, name, age

FROM students

WHERE age >= 10 OR name = 'John';''',
    '''SELECT id, name, age

FROM students

WHERE age >= 10 AND name = 'John';''',
    '''SELECT DISTINCT name, color

FROM clothing;''',
    '''SELECT id, name

FROM animal

ORDER BY name DESC, id;''',
    '''SELECT name, color

FROM clothing

WHERE color != NULL;''',
    '''SELECT id, name

FROM animal

ORDER BY name;''',
    '''SELECT Name, ProductNumber, ListPrice AS Price
FROM Production.Product 
WHERE ProductLine = 'R' 
AND DaysToManufacture < 4
ORDER BY Name ASC;''',
    '''SELECT SUM (price)

FROM product;''',
    '''SELECT last_name FROM customer

INTERSECT

SELECT last_name FROM employee;'''
]