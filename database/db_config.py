import mysql.connector
from mysql.connector import errorcode


class database():

    def sql(self, sql_query):

        try:
            config = {
                'user' : 'root',
                'password' : '1111',
                'host' : '127.0.0.1',
                'database' : 'northwind'}

            cnx = mysql.connector.connect(**config)
            my_cursor = cnx.cursor()
            my_cursor.execute(sql_query)
            cnx.close()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        else:
            cnx.close()

        return my_cursor.fetchall()