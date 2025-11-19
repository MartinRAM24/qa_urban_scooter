import psycopg2

def conectar():
    return psycopg2.connect(host="127.0.0.1", port="5555", user="morty", password="smith", database="scooter_rent")

def buscar_courier_por_login(login: str):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM courier WHERE login = %s", (login,))
    data = cur.fetchone()
    cur.close()
    conn.close()
    return data

def assert_courier_en_db(login: str):
    row = buscar_courier_por_login(login)
    assert row is not None, f"Courier con login '{login}' NO está en la BD"

def assert_courier_no_existe_en_db(login: str):
    row = buscar_courier_por_login(login)
    assert row is not None, f"Courier con login '{login}' Todavia existe en la BD"

def orders_for_courier_in_db(courier_id: int):
    conn = conectar()
    cur = conn.cursor()
    # Ajusta el nombre de la tabla si es distinto
    cur.execute("SELECT id FROM orders WHERE courier_id = %s;", (courier_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows