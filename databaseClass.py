import mysql.connector

### pip install python-dotenv
from dotenv import load_dotenv

### Cargar variables de entorno del archivo .env
load_dotenv()

import os

### traer las variables de entorno
DBUSER = os.getenv("DATABASE_USER")
DBPASSWORD = os.getenv("USER_PASSWORD")
DBNAME = os.getenv("DATABASE_NAME")
DBHOST = os.getenv("DATABASE_HOST")

class Note:
    def __init__(self,title,description,id=None):
        self.id = id
        self.title = title
        self.description = description

class Db:
    ### contrucstor de la base de datos
    def __init__(self) :
        self.db_connection = mysql.connector.connect(
            host = DBHOST,
            user = DBUSER,
            password = DBPASSWORD,
            database = DBNAME
        )
        self.cursor = self.db_connection.cursor()
    
    def insertNote(self,title,description):
        sql = "INSERT INTO notas (titulo, descripcion) VALUES (%s,%s)"
        values = (title,description)

        self.cursor.execute(sql,values)
        self.db_connection.commit()

    def getNotas(self):
        sql = "SELECT * FROM notas"

        self.cursor.execute(sql)
        
        resolve = self.cursor.fetchall()
        notas = []

        for res in resolve:
            id,titulo,descripcion = res
            nota = Note(titulo,descripcion,id)
            notas.append(nota)
        return notas
    
    def deleteNote(self,id):
        sql = "DELETE FROM notas WHERE id = %s"
        
        self.cursor.execute(sql,(id,))

        self.db_connection.commit()

    def updateNote(self,title,description,id):
        sql = "UPDATE notas SET titulo = %s, descripcion = %s WHERE id = %s"
        values = ( title, description, id )

        self.cursor.execute(sql,values)
        self.db_connection.commit()


    ### cerrando conexion
    def closeSession(self):
        self.cursor.close()
        self.db_connection.close()

