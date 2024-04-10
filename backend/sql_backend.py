import sys
import mariadb


conn = mariadb.connect(
    user="root",
    password="Mysql123",
    host ="127.0.0.1",
    port=3306,
    database="jj_ctf"
)  
cur = conn.cursor()

def sjekk_flagg():
    by = input("Skriv inn navnet på byen du sjekker flagget for: ")
    flagg = input("Skriv inn flagget du skal sjekke om er riktig: ")
    cur.execute("select * from flagg where name=%s and ctf_flagg=%s", (by, flagg))
    for row in cur:
        text = ''
        for value in row:
            text+=str(value) + '\t\t'
        print(text)

conn.commit()

cur.close()
 