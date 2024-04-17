import sqlite3

conn=sqlite3.connect("personal_db.db")

print("\nEMPLEADOS: INNER JOIN")
cursor = conn.execute(
    """SELECT EMPLEADOS.nombre, SALARIOS.salario 
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id=EMPLEADOS.id
    """
)

for row in cursor:
    print(row)

conn.execute(
    """
    UPDATE EMPLEADOS
    SET cargo_id = '3'
    WHERE id = 2
    """
)
conn.execute(
    """
    UPDATE SALARIOS
    SET empleado_id = '1'
    WHERE id = 1
    """
)
def imprimir ():    
    print("\nCAMBIAR")
    imprimir=conn.execute(
        """
        SELECT * FROM EMPLEADOS
        """
    )
    for row in imprimir:
        print(row)
    print("\nEMPLEADOS: INNER JOIN")
    cursor = conn.execute(
        """SELECT EMPLEADOS.nombre, SALARIOS.salario 
        FROM SALARIOS
        JOIN EMPLEADOS ON SALARIOS.empleado_id=EMPLEADOS.id
        """
    )

    for row in cursor:
        print(row)

print("\nELIMINAR")
conn.execute(
    """
    DELETE FROM EMPLEADOS
    WHERE id = 2
    """
)
imprimir()
conn.close()