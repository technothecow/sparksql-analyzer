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

SELECT last_name FROM employee;''',
    'CREATE DATABASE test_db COMMENT \'123\' LOCATION \'test_db.sparksql\' WITH DBPROPERTIES(good=True);',
    '''CREATE TABLE student (id INT, name STRING, age INT) STORED AS ORC;''',
    '''CREATE TABLE student_copy STORED AS ORC
    AS SELECT * FROM student;''',
    '''CREATE TABLE student (id INT, name STRING, age INT)
    COMMENT 'this is a comment'
    STORED AS ORC
    TBLPROPERTIES ('foo'='bar');''',
    '''CREATE TABLE student (id INT, name STRING)
    PARTITIONED BY (age INT)
    STORED AS ORC;''',
    '''CREATE EXTERNAL TABLE family(
        name STRING,
        friends ARRAY<STRING>,
        children MAP<STRING, INT>,
        address STRUCT<street: STRING, city: STRING>
    )
    STORED AS TEXTFILE
    LOCATION '/tmp/family/';''',
    '''CREATE TABLE clustered_by_test2 (ID INT, NAME STRING)
    PARTITIONED BY (YEAR STRING)
    CLUSTERED BY (ID, NAME)
    SORTED BY (ID ASC)
    INTO 3 BUCKETS
    STORED AS PARQUET;''',
    '''CReatE DATABASE IF NOT EXISTS db_name 
    COMMENT 'sample comment'
    LOCATION 'path/to/the/file.db'
    with DBPROPERTIES(prop1=val1,prop2=val2);
    '''
]