from app_flask.configuraciones.mysqlconnection import connectToMySQL
from app_flask import BASE_DATOS

class Ninja:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.age = datos['age']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.id_dojo = datos['id_dojo']
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO ninjas(nombre, apellido, age, id_dojo)
                VALUES(%(nombre)s,%(apellido)s,%(age)s,%(id_dojo)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)