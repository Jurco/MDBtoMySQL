import sys
import pyodbc
import mysql.connector
from mysql.connector import errorcode

config = {
	'user': 'root',
	'password': '4ere3ne',
	'host': '127.0.0.1',
	'database': 'exec',
	'raise_on_warnings': True,
}

# open connectio to MDB database
# param db: data file path	
# return: connection to db
def odbc_open_connection(db):
	con_string = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=' + db
	try:
		conn = pyodbc.connect(con_string, autocommit=True)
	except pyodbc.Error as err:
			print err
	else:
		print "Connected to MDB"
	return conn
	
# close connection to MDB database
# param connector: connection to db
def odbc_close_connection(connector):
	try:
		connector.close()
	except pyodbc.Error as err:
		print err
	else:
		print "Disconnected from MDB"
		
# open connectio to MySQL database
# return: connection to db		
def mysql_open_connection():
	try:
		conn = mysql.connector.connect(**config)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with your user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exists"
		else:
			print err
	else:
		print "Connected to MySQL"
	return conn
	
# close connection to MySQL database
# param connector: connection to db
def mysql_close_connection(connector):
	try:
		connector.close()
	except mysql.connector.Error as err:
		print err
	else:
		print "Disconnected from MySQL"

# query to odbc database 
# param cursor: odbc connection currsor
# param query: sql string query
# return: query result
def odbc_query(cursor, query):
	return cursor.execute(query)
		
if __name__ == '__main__':

	mysql_connector = mysql_open_connection()
	odbc_connector = odbc_open_connection('g:\data.mdb')
	
	odbc_curr = odbc_connector.cursor()
	
	data = odbc_query(odbc_curr, 'select * from table1')
	for row in data:
		print str(row) + "\n"
	
	odbc_close_connection(odbc_connector)
	mysql_close_connection(mysql_connector)
	