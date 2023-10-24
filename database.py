import mysql.connector

from dotenv import load_dotenv

load_dotenv()

import os

DBUSER = os.getenv("DATABASE_USER")
DBPASSWORD = os.getenv("USER_PASSWORD")
DBNAME = os.getenv("DATABASE_NAME")
DBHOST = os.getenv("DATABASE_HOST")

db_connection = mysql.connector.connect(
    host = DBHOST,
    user = DBUSER,
    password = DBPASSWORD,
    database = DBNAME
)

cursor = db_connection.cursor()
def insert(cursor):
    titulo = "Title"
    descripcion = "Description"

    sqlQuery = "INSERT INTO notas (titulo,descripcion) VALUES (%s, %s)"
    values = (titulo, descripcion)

    cursor.execute(sqlQuery,values)

    db_connection.commit()

def showTable(cursor):
    sql = "SELECT * FROM notas"

    cursor.execute(sql)

    res = cursor.fetchall()

    for row in res:
        id, titulo, descripcion = row
        print(f"ID:{id}\tTitulo:{titulo}\tdescripcion:{descripcion}")

# Cierra el cursor
cursor.close()

# Cierra la conexión
db_connection.close()
