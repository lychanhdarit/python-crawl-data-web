import mysql.connector
from mysql.connector import Error 

class DataContext:  

    def __init__(self):
        self.connect = mysql.connector.connect(host='localhost', database='bookbank', user='root',  password='vinasave@123')

    #get connection
    @staticmethod
    def connectionProvider():
        return mysql.connector.connect(host='localhost', database='bookbank', user='root',  password='vinasave@123')
    #get Data
    def getData(self, sql):
        try:
            connection = self.connect
            if connection.is_connected():
                mycursor = connection.cursor()
                mycursor.execute(sql) 
                #result = mycursor.fetchall()
                for item in mycursor:
                    print(item) 
                return mycursor
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                mycursor.close()
                connection.close()
                print("MySQL connection is closed")
    #Insert multi row
    def insertMultiRowData(self, sqlform, dataArray):
        try:
            mydb = self.connect
            if mydb.is_connected():
                mycursor = mydb.cursor() 
                mycursor.executemany(sqlform,dataArray)
                mydb.commit()
                print("Insert success!")
        except Error as e:
            print("Error while connecting to MySQL", e)
        ''' finally:
            if (mydb.is_connected()):
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed") '''
    #Update 1 row
    def updateData(self, sql):
        try:
            mydb = self.connect
            if mydb.is_connected():
                mycursor = mydb.cursor() 
                mycursor.execute(sql)
                mydb.commit()
                print("Update success!")
        except Error as e:
            print("Error while connecting to MySQL", e)
        ''' finally:
            if (mydb.is_connected()):
                mycursor.close()
                mydb.close()
                print("MySQL connection is closed") '''
    #Insert 1 row
    def insertData(self, sql):
        try:
            mydb = self.connect
            if mydb.is_connected():
                mycursor = mydb.cursor() 
                mycursor.execute(sql)
                mydb.commit()
                print("Insert 1 row success!")
        except Error as e:
            print("Error while connecting to MySQL", e)
        ''' finally: '''
        '''     if (mydb.is_connected()): '''
        '''         mycursor.close() '''
        '''         mydb.close() '''
        '''         print("MySQL connection is closed") '''
     