import mysql.connector
from datetime import date
import passwd

class connect_DataBase:
    def __init__(self,Host,username,PassWord,Port,database_name):
        self.connection = mysql.connector.connect(host=Host,
                                                  user=username,
                                                  passwd=PassWord,
                                                  port=Port,
                                                  database=database_name)
    
    def Select_one(self,search,table,column,id_search):
        try:
            cursor = self.connection.cursor()
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
            cursor = self.connection.cursor()
            sql = "SELECT {} FROM {}".format(search, table)
            cursor.execute(sql)
            data = cursor.fetchall()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return data
        
    def last_id(self, search, table):
        try:
            cursor = self.connection.cursor()
            sql = f"SELECT MAX( {search} ) FROM {table};"
            cursor.execute(sql)
            data = cursor.fetchone()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()
            return data[0]

class employee(connect_DataBase):

    def Add(self,id,rfc,name,email,phone,addres,post):
        try:
            cursor = self.connection.cursor()
            sql = f"INSERT INTO empleado(idempleado,rfc,nombre,correo,telefono,direccion,cargo,fecha_contratacion) VALUES ({id},'{rfc}','{name}','{email}',{phone},'{addres}','{post}','{date.today()}');"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def modifier(self, id, rfc, name, email, phone, addres, post):
        try:
            cursor = self.connection.cursor()
            sql = f"UPDATE empleado SET rfc = '{rfc}', nombre = '{name}', correo = '{email}', telefono = {phone}, direccion = '{addres}', cargo = '{post}' WHERE idempleado = {id};"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def leave(self,id):
        try:
            cursor = self.connection.cursor()
            sql = f"UPDATE empleado SET fecha_baja = '{date.today()}' WHERE idempleado = {id};"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()


class product(connect_DataBase):

    def Add(self,id,name,price,stock):
        try:
            cursor = self.connection.cursor()
            sql = f"INSERT INTO producto(idproducto,nombre,precio,stock) VALUES ({id}, '{name}', {price}, {stock});"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def Modifier(self,id,name,price,stock):
        try:
            cursor = self.connection.cursor()
            sql = f"UPDATE producto SET nombre = '{name}', precio = {price}, stock = {stock} WHERE idproducto = {id};"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def Delete(self,id):
        try:
            cursor = self.connection.cursor()
            sql = f"DELETE FROM producto WHERE idproducto = {id}"
            cursor.execute(sql)
            self.conecction.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

class membership(connect_DataBase):
    def Add(self,id, name, email, type):
        try:
            cursor = self.connection.cursor()
            sql = f"INSERT INTO membresia(idmembresia, nombre, email, tipo, fecha_alta, puntos) VALUES({id}, '{name}', '{email}', '{type}', '{date.today()}', 0);"
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def Modifier(self, id, name, email, type):
        try:
            cursor = self.connection.cursor()
            sql = f"UPDATE membresia SET nombre = '{name}', email = '{email}', tipo = '{type}' WHERE idmembresia = {id};"
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()

    def Leave(self, id):
        try:
            cursor = self.connection.cursor()
            sql = f"UPDATE membresia SET fecha_baja = '{date.today()}' WHERE idmembresia = {id};"
            cursor.execute(sql)
            self.connection.commit()
        except Exception as Ex:
            print(Ex)
        finally:
            cursor.close()