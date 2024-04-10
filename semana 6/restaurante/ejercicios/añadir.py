import sqlite3

conn = sqlite3.connect("personal_db.db")
def insertdepartamento(name,pepito):
    conn.execute(
        f"""
        INSERT INTO DEPARTAMENTOS(nombre,fecha_creacion) 
        VALUES ('{name}', '{pepito}')
        """
    )

def insertcargo(nombre, nivel ,fecha_creacion):
    conn.execute(
        f"""
        INSERT INTO CARGOS(nombre,nivel,fecha_creacion) 
        VALUES ('{nombre}','{nivel}','{fecha_creacion}')
        """
    )
insertdepartamento("ventas","10-04-2020")
insertdepartamento("Marketing","11-04-2020")

insertcargo("Senior","Analisis de marketing","10-04-2020")
insertcargo("Junior","Analisis de marketing","10-04-2020")

conn.commit()

conn.close
