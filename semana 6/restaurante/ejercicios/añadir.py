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
    
def insertempleado(nombre,ap1 ,ap2,fechacon,depid,carid,fechcrea):
    conn.execute(
        f"""
        INSERT INTO EMPLEADOS(nombre,apellido_paterno,apellido_materno,fecha_conteratacion,departamento_id,cargo_id,fecha_creacion) 
        VALUES ('{nombre}','{ap1}','{ap2}','{fechacon}','{depid}','{carid}','{fechcrea}')
        """
    )
def insertarsalario(empleado,salario,ini,fin,creacion):
    conn.execute(
        f"""
        INSERT INTO SALARIOS(empleado_id,salario,fecha_inicio,fecha_fin,fecha_creacion)
        VALUES('{empleado}','{salario}','{ini}','{fin}','{creacion}')
        """
    )
#insertdepartamento("ventas","10-04-2020")
#insertdepartamento("Marketing","11-04-2020")

#insertcargo("Senior","Analisis de marketing","10-04-2020")
#insertcargo("Junior","Analisis de marketing","11-04-2020")
#insertcargo("Junior","Representante de Ventas","12-04-2020")

insertempleado("Juan","Gonzales","Lopez","15-05-2023","1","3","15-05-2023")
insertempleado("Maria","Lopez","Martinez","20-06-2023","2","2","15-05-2023")
insertarsalario("1",'3000',"01-04-2024","30-04-2025","01-04-2024")
insertarsalario("2",'3500',"01-07-2023","30-04-2024","01-07-2023")

conn.commit()

conn.close
