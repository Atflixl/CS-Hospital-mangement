# Basic SQL Commands
## How to create a database:
```SQL
CREATE DATABASE <db name>;
```

## To see all databases in mysql (registered to user):
```sql
SHOW DATABASES;
```
## To see which database is activated:
```sql
SELECT DATABASE();
```

## To create a table:
```sql
CREATE TABLE <table name>(
<key name> <value type>(<size>),(comma IF more)
);
```

## To see a table structure:
```sql
DESC <table name>;
```

## To see all tables inside a database:
```sql
SHOW TABLES;
```

## To enter data into a table:
```SQL
INSERT INTO <table name>(<row names comma seperated to add data to specific row>) VALUES(<comma seperated values as per column order>)<add comma and continue adding as tuple for multiple values>
```

## How to query:
```SQL
SELECT <columns, comma seperated> FROM <table name>
```

### To see all values inside the given table:
```SQL
SELECT * FROM <table name>
```

## To select db :
```SQL
USE <database>;
```

## To select values from a table meeting a condition
```SQL
SELECT * FROM <TABLE> WHERE <CONDITION>
```
## To delete a database/table
```SQL
DROP <table/database name>
```

### Update given record
```SQL
update <table name> set <row name>=<value> where <condition>;
```

# To delete an entry
```sql
DELETE FROM <TABLE NAME> WHERE <CONDITION>;
```
## Modify a table to add a column
#### Add a column at the end
```SQL
ALTER TABLE <table name> ADD COLUMN <name> <data type/size>
```
#### Add a column after a given columns
```SQL
ALTER TABLE <table name> <column name> <data type/size> AFTER <column name>
```
#### Add a column at the top
```SQL
ALTER TABLE <table name> <name> <data type/size> FIRST
```
ALTER TABLE <EMP> <name> <data type/size> AFTER <column nmae>

ALTER TABLE <EMP> <name> <data type/size> FIRST

ALYER TABLE <EMP> DROP <COLUMN>

# Possible SQL Value types
- **INT** : takes small integer
- **CHAR** : stores string as length given (for example 8bytes for _INT(8)_)
- **VARCHAR** : stores data as length given by user
- **DATE** : stores interger as date form. Takes in integer as _YYYYMMDD_
- **NUMERIC** : takes in long integer, float, etc.

# SQL Constraints
- primary key
- foreign key
- unique
- default
- not null   

# SQL Operators
## Arithemetic Operator:
- + : EXAMPLE : ``UPDATE EMP SET ID=ID+100``
- - : EXAMPLE : ``UPDATE EMP SET ID=ID-100``
## Relational Operator:
- >
- <
- =
- IN() || Example : `` select * from <table name> where <row name> in(comma seperated values which should exist)``
- OR
- AND
- BETWEEN <1st no> and <2nd no> : range (both nos are inclusive)
- IS NULL
- IS NOT NULL
- LIKE '%<ENDING>' : here anything after **%** means if value is ending with <ENDING>
- LIKE '<STARTING>%' : here anything before **%** means if value is starting with <STARTING>
    - LIKE takes 2 special characters:
        - % : for multiple values
        - _ : for a single value
            - Example : LIKE 'SM_TH' -- will return all values which start with SM, end with TH and have 5 chars in total. (IE. SMITH, SMETH, SMATH)




UPDATE <EMP> SET <columen>=<value> WHERE <index>=<value>
