import psycopg2
def insert_or_update_user(name, phone):
    with psycopg2.connect(host="localhost", database="PhoneBook", user="postgres", password="12052006") as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            conn.commit()
            print("Added or updated.")

insert_or_update_user("Асан", "+77777777777")