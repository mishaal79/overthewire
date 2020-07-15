# Password to level
AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J

# Problem
SQLinjection on  website
No sanitisation of input

SQL condition is used in query with where clause to get user and password match

# Solution
Use sqlinjection to perform a logic bomb on the query string.
Query = Select from table Where conditon1 and condition2;
Insert an OR condition at the end of query with a true statement.
Overall the query will look like
Query = Select form table where (condition1 and condition2) OR condition3;
therefore when condition3 is always true, query will return results.

# Learnings 

# Mitigation
