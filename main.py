import sqlite3
#create database connection
connection=sqlite3.connect('mydatabase.db', timeout=10)
#collect data 
fname=input('ENTER YOUR FIRST NAME :')
sname=input('ENTER YOUR SECOND NAME :')
email=input('ENTER YOUR EMAIL :')
password=input('ENTER YOUR PASSWORD :')
#make a query to send or insert data into the databse
with connection:
    query=connection.cursor()
    #using sql query to insert
    query.execute("insert into users values(?,?,?,?);",(fname,sname,email,password))   
    connection.commit()
#query to select all data from the database to collect data and display all
query.execute("select * from users")
rows=query.fetchall()
print(rows)