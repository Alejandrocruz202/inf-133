import sqlite3

conn = sqlite3.connect("restaurant.db")
def insertpalto(name,prec,categoria):
    conn.execute(
        f"""
        INSERT INTO PLATOS(nombre, precio, categoria) 
        VALUES ('{name}', '{prec}', '{categoria}')
        """
    )

def insertmesa(num):
    conn.execute(
        f"""
        INSERT INTO MESAS(numero) 
        VALUES ('{num}')
        """
    )

def insertPedido(plato,mesa,cantidad,fecha):
    conn.execute(
        f"""
        INSERT INTO PEDIDOS(plato_id,mesa_id,cantidad,fecha)
        VALUES('{plato}','{mesa}','{cantidad}','{fecha}')
        """
    )


insertpalto('pizza','10.90','italiana')
insertpalto('hamburguesa','8.99','Americana')
insertpalto('sushi','12.99','japonesa')
insertpalto('ensalada','6.90','vegetariana')

insertmesa('1')
insertmesa('2')
insertmesa('3')
insertmesa('4')

insertPedido('1','2','2','2024-04-01')
insertPedido('2','3','1','2024-04-01')
insertPedido('3','1','3','2024-04-02')
insertPedido('4','4','1','2024-04-02')


conn.commit()
conn.close
