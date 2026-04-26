from samba.samba3.mdscli import conn

cur = conn.cursor()
cur.execute("SELECT * FROM productos")
registros = cur.fetchall()
cur.close()

for r in registros:
    idx, desc, precio = r
    print("identificador: {}".format(idx))
    print("\tdescripción: {}".format(desc))
    print("\tprecio: {}".format(precio))