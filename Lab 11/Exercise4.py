import psycopg2
def get_paginated_records(limit, offset):
    with psycopg2.connect(host="localhost", database="PhoneBook", user="postgres", password="12052006") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated_phonebook(%s, %s)", (limit, offset))
            print(f"Записи (limit={limit}, offset={offset}):")
            for row in cur.fetchall():
                print(row)

get_paginated_records(2, 1)