This folder contain :

1) create_tables_mysql_rds.ipynb
- Allows to create table in the mysql database in aws rds

2) inject_aws_mysql.py
- Allows to automatically inject data from dataframe into the diffrent sql table stored in the cloud (aws rds)

3) sql_queries_rds.ipynb
- Allows to queries our mysql database stored in aws rds

4) function_test.py
- Functions to allows unit testing :
- a. test the connection to the database
- b. test data fetching from mysql databse 

5) test_pytest.py
- Run the unit test above with pytest (this pytest file is automatically run after a push with github actions)
