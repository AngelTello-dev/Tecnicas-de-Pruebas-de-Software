import psycopg2

def connect():
    try:
        # conectando al servidor de PostgreSQL
        conn = psycopg2.connect(
                            host="localhost",
                            database="sistema_abc",
                            user="uacm",
                            password="uacm1"
                        )
        print('Conectado con el Servidor de PostgreSQL')
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


conn = connect()