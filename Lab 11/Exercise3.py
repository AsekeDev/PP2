import psycopg2
def insert_many_users(names, phones):
    with psycopg2.connect(host="localhost", database="PhoneBook", user="postgres", password="12052006") as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
            conn.commit()
            print("Insert completed.")
            
names = ["Асан","Нурик","Бека",]
phones = ["+77085471775", "+77770007777","+77757760000"]
insert_many_users(names, phones)