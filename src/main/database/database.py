import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Doughnut59@+Scits",
    database="testDatabase"
)

cursor = db.cursor()

## implement into app!