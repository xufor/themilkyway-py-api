import psycopg2

ADMIN_UID = '26e1a2'
ADMIN_HASH = '$2b$12$ldy3v6k0TLT3cBT8UQmEAO6WZiJ3xHarDKuA8cbCcy4UgpCvyVaku'
ADMIN_REG_TIME = '2019-06-16 17:34:35.000000'
ADMIN_NAME = 'Admin'
ADMIN_EMAIL = 'admin@mail.com'
ADMIN_PASSWORD = '48c5ae'


def create_admin_user():
    conn = psycopg2.connect(dbname='themilkyway', user='postgres', password='1999')
    cur = conn.cursor()
    cur.execute('INSERT INTO active (uid, time, name, email, password) VALUES (%s, %s, %s, %s, %s)',
                (ADMIN_UID, ADMIN_REG_TIME, ADMIN_NAME, ADMIN_EMAIL, ADMIN_HASH))
    conn.commit()
    cur.close()
    conn.close()
