import psycopg2


conn = psycopg2.connect(
    dbname="project",
    user="postgres",
    password="Amrita@1988",
    host="localhost",  # Change to your server if needed
    port="5432"  # Default PostgreSQL port
)

cur = conn.cursor()


cur.execute("SELECT * from users")


print(cur.fetchone())



cur.close()
conn.close()