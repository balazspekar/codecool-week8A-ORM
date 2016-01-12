# Object-relational mapping
## Codecool Task
#### Week 8A

Your task is to do the followings:
We would like to represent the database content as objects in an object oriented language like the python. Object-relational mapping (ORM) is a technique (a.k.a. design pattern) of accessing a relational database from an object-oriented language (Java, python for example).

Application:
GitHub repository is needed.
Test are not mandatory.

Create a python application which can import data from a CSV file, parses the containing data to objects and stores the data in MySQL database. The application has to be able to export data from database to CSV file. The application uses the previusly created NorthwindDB. Import and export functions are limited to use these tables: Employees, Customers, Orders and OrderDetails so you don't need to create a class for every tables in the DB !
All of the classes should contain a static parse() method which require a string as a parameter (CSV row) and creates (and returns) an object from it.
The classes should contain a persist() method (procedure) with no parameter.
Define a to_csv() method which returns a string representation of the current object which can be written out as a CSV row.
OPTIONAL: Define a function (in every class), called select(), which generates and runs a basic SQL select operation. The method gets a string parameter where you can define which field you want to be selected, a named boolean parameter, called distinct (default False) which means if the selected field should be distinct and a named string parameter where, which means if you want your result to be filtered with the given conditions.
OPTIONAL: Create a basic menu where user can use the features above.
E.g.

Import from CSV : Sub-menu >Employees, Customers, Orders, Orders and details
Export to CSV : Sub-menu >Employees, Customers, Orders, Orders and details
List table : Sub-menu >Employees, Customers, Orders, Orders and details