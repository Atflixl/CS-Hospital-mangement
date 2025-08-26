import mysql.connector as sql

con = sql.connect(host="localhost", user="dapc", passwd="admin", database="hospital")
csr = con.cursor()
