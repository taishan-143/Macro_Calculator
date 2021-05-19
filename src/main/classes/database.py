import mysql.connector 

db = mysql.connector.connect(
    host="localhost",
    user="Taishan",
    passwd="Doughnut59@+Scits",
    database="",
    auth_plugin="mysql_native_password"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE testDatabase")


### sort out issue ###