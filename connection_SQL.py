import mysql.connector
from datetime import date


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
            sql = "SELECT {} FROM {}".format(search, table)
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return data

class employee(connect_DataBase):

    def Add(self,id,rfc,name,email,phone,addres,post):
        try:
            cursor = self.conecction.cursor()
            sql = f"INSERT INTO empleado(idempleado,rfc,nombre,correo,telefono,direccion,cargo,fecha_contratacion) VALUES ({id},'{rfc}','{name}','{email}',{phone},'{addres}','{post}','{date.today()}');"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def modifier(self, id, rfc, name, email, phone, addres, post):
        try:
            cursor = self.conecction.cursor()
            sql = f"UPDATE empleado SET rfc = '{rfc}', nombre = '{name}', correo = '{email}', telefono = {phone}, direccion = '{addres}', cargo = '{post}' WHERE idempleado = {id};"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def leave(self,id):
        try:
            cursor = self.conecction.cursor()
            sql = f"UPDATE empleado SET fecha_baja = '{date.today()}' WHERE idempleado = {id};"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()