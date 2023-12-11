import mysql.connector


class connect_DataBase:
    def __init__(self,Host,username,PassWord,Port,database_name):
        self.conecction = mysql.connector.connect(host=Host,
                                                  user=username,
                                                  passwd=PassWord,
                                                  port=Port,
                                                  database=database_name)
    
    def Select_one(self,search,table,column,id_search):
        try:
            cursor = self.conecction.cursor()
            sql = f"SELECT {search} FROM {table} WHERE {column} = {id_search}"
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return data
    
    def Select_all(self, search, table):
        try:
            cursor = self.conecction.cursor()
            sql = "SELECT '{}' FROM '{}'".format(search, table)
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return data
