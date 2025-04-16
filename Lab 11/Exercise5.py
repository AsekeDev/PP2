import psycopg2

def delete_data(name, phone):
    with psycopg2.connect(host="localhost", database="PhoneBook", user="postgres", password="12052006") as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_data(%s, %s)", (name, phone))
            conn.commit()
            print("Removal completed.")
delete_data(None, "+77085471775")