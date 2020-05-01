import mysql.connector
import sys
#This python program replaces a table with an equal yet empty version of itself.  
#usage is python purge.py tablename hostname username password
#After that, an empty version of the previous table will be made
table = sys.argv[1]
hostname = sys.argv[2]
username = sys.argv[3]
password= sys.argv[4]
mydb = mysql.connector.connect(
  host=hostname,
  user=username,
  passwd=password,
  database=table
)
#This connects the database to the correct database.  
#Next, we find the names of the columns in the table
mycursor = mydb.cursor()
values= cursor.column_names
#Next, we delete the table
sql = ("DROP TABLE" + table)
mycursor.execute(sql)
#Next, we create an identical table with same table name
Input = "CREATE TABLE " + table + " (" + values[0] + "VARCHAR(255))"
mycursor.execute(Input)
i=1
while(i<length(values)):
	Input=("ALTER TABLE " + table + "ADD " + values[i] + " VARCHAR(255))")
	mycursor.execute(Input)
	i=i+1
Input.append("))")
