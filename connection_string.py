import mysql.connector as sql

con = sql.connect(host="192.168.1.11", user="dapc", passwd="admin", database="reliance")
csr = con.cursor()
"""
eid=input('Enter the ID: ')
ename=input('Enter the Name: ')
edoj=input('Enter the Joining Date: ')
esal=int(input('Enter the Salary: '))
edept=input('Enter the Department: ')

qry="INSERT INTO EMP VALUES('{}','{}','{}',{},'{}');".format(eid,ename,edoj,esal,edept)
csr.execute(qry)
"""
dept = input("Enter the Department: ")
qry = "SELECT * FROM EMP WHERE employeedept='{}';".format(dept)
csr.execute(qry)

data = csr.fetchall()
print(type(data))
print(data)

for x in data:
    print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t", x[4], "\t")

con.commit()
