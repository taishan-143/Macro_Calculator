import mysql.connector

def database_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Doughnut59@+Scits",
        database="macronutrientbase"
    )
    return connection

## implement into app!

class Data_Persistence:

    def save_user_to_database(self, user_data):
        try:
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute("INSERT INTO User (name, age, sex, weight, height) VALUES (%s, %s, %s, %s, %s)", user_data)
            connection.commit()
            cursor.close()
        except Exception as e:
            print("\nFailure uploading data to the database: ")
            print(e)
        finally:
            connection.close()    

    def load_data_from_database(self, data_type, target_data_type, target_data_value):
        try:
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT "f"{data_type}"" FROM User WHERE "f"{target_data_type}"" = %s", target_data_value)
            connection.commit()
            cursor.close()
        except Exception as e:
            print("\nFailure loading data from the database: ")
            print(e)
        finally:
            connection.close() 

    def remove_user_from_database(self, users_name):
        try:
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM User WHERE name = %s", users_name)
            connection.commit()
            cursor.close()
        except Exception as e:
            print("\nFailure removing user from the database")
            print(e)
        finally:
            connection.close() 

    def update_value_in_database(self, data_type, data_value, target_data_type, target_data_value):
        try:
            values = [data_value, target_data_value]
            connection = database_connection()
            cursor = connection.cursor()
            cursor.execute("UPDATE User SET "f"{data_type}"" = %s WHERE "f"{target_data_type}"" = %s", values)
            connection.commit()
            cursor.close()
        except Exception as e:
            print("\nFailure updating the database")
            print(e)
        finally:
            connection.close() 
    
    def create_register(self):
        try:
            connection = database_connection()
            cursor = connection.cursor(buffered=True)
            cursor.execute("SELECT name FROM User")
            connection.commit()
            people = cursor.fetchall()
            cursor.close()
            
        except Exception as e:
            print("\nFailure reading names from the database: ")
            print(e)
        finally:
            connection.close() 

        names = []
        for person in people:
            names.append(person[0])
        return names


dp = Data_Persistence()
test = dp.load_data_from_database("age", "name", "T dog")