from database.db_config import database

# instantiating an object which communicates with the database
db = database()

result = db.sql('SELECT CONCAT(LastName, " ", FirstName), Title FROM employees')
print(result)
print(len(result))