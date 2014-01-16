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

"""
def odbc():
      
    constr = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=' + db
    conn = pyodbc.connect(constr, autocommit=True)
    cur = conn.cursor()
    strsql = "select * from table1"
    cur.execute(strsql)
    t = list(cur)
    conn.close()
    return t
"""	
	
def odbc_open_connection(db):
	con_string = 'Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=' + db
	try:
		conn = pyodbc.connect(con_string, autocommit=True)
	except pyodbc.Error as err:
			print err
	else:
		print "Connected to MDB"
	return conn
	
def odbc_close_connection(connector):
	try:
		connector.close()
	except pyodbc.Error as err:
		print err
	else:
		print "Disconnected from MDB"
		
def mysql_open_connection():
	try:
		cnx = mysql.connector.connect(**config)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print "Something is wrong with your user name or password"
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print "Database does not exists"
		else:
			print err
	else:
		print "Connected to MySQL"
	return cnx
	
def mysql_close_connection(connector):
		try:
			connector.close()
		except mysql.connector.Error as err:
			print err
		else:
			print "Disconnected from MySQL"
		
if __name__ == '__main__':

	mysql_connector = mysql_open_connection()
	odbc_connector = odbc_open_connection('g:\data.mdb')
	
	odbc_curr = odbc_connector.cursor()
	strsql = "select * from table1"
	data = odbc_curr.execute(strsql)
	
	for row in data:
		print str(row) + "\n"
	
	odbc_close_connection(odbc_connector)
	mysql_close_connection(mysql_connector)
	