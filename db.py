import sqlite3


# Crea un módulo
def create_database():
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Crea una tabla si no existe
    cur.execute("""CREATE TABLE IF NOT EXISTS setting (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    broker           TEXT,
    port             TEXT,
    topic_subscriber TEXT,
    topic_publisher  TEXT
    )""")

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()

# Obtiene todas las configuraciones de la base de datos
def get_setting():
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Obtiene todos las configuraciones
    setting = cur.execute("""SELECT * FROM setting""").fetchall()

    # Cierra la conexión a la base de datos
    conn.close()

    return setting

# Agrega un registro
def add_setting(broker, port, topic_subscriber, topic_publisher):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Inserta el nuevo registro
    cur.execute("""INSERT INTO setting (broker, port, topic_subscriber, topic_publisher) VALUES (?, ?, ?, ?)""", (broker, port, topic_subscriber, topic_publisher))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()    

# Actualiza broker
def update_broker(id, broker):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Actualiza los campos de la tabla "setting" utilizando los parámetros proporcionados
    cur.execute("""UPDATE setting SET broker = ? WHERE id = ?""",
                (broker, id))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()

# Actualiza broker
def update_port(id, port):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Actualiza los campos de la tabla "setting" utilizando los parámetros proporcionados
    cur.execute("""UPDATE setting SET port = ? WHERE id = ?""",
                (port, id))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()


# Actualiza topic_subscriber
def update_topic_subscriber(id, topic_subscriber):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Actualiza los campos de la tabla "setting" utilizando los parámetros proporcionados
    cur.execute("""UPDATE setting SET  topic_subscriber = ? WHERE id = ?""",
                ( topic_subscriber, id))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()


# Actualiza topic_publisher
def update_topic_publisher(id, topic_publisher):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Actualiza los campos de la tabla "setting" utilizando los parámetros proporcionados
    cur.execute("""UPDATE setting SET  topic_publisher = ? WHERE id = ?""",
                ( topic_publisher, id))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()


# Elimina un registro
def delete_setting(id):
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Elimina el resitro
    cur.execute("""DELETE FROM setting WHERE id = ?""", (id,))

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()

# Agrega un método para eliminar todos los registros
def delete_all_setting():
    # Crea una conexión a la base de datos
    conn = sqlite3.connect("database.db")

    # Crea un cursor para ejecutar consultas SQL
    cur = conn.cursor()

    # Elimina todos los registros
    cur.execute("""DELETE FROM setting""")

    # Guarda los cambios
    conn.commit()

    # Cierra la conexión a la base de datos
    conn.close()