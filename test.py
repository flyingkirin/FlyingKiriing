import pyodbc
conn=pyodbc.connect("DSN=AGSMulti_fly;UID=sfim;pwd=ramol$fo")
cursor=conn.cursor()
cursor.execute("select distinct file_no from sfim.flight_list")
for row in cursor:
    print row.file_no
