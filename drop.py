import psycopg2


def drop_all_tables():
    conn = psycopg2.connect(dbname='themilkyway', user='postgres', password='1999')
    cur = conn.cursor()
    cur.execute('DROP TABLE "like"')
    cur.execute('DROP TABLE VIEWS')
    cur.execute('DROP TABLE FOLLOW')
    cur.execute('DROP TABLE STORIES')
    cur.execute('DROP TABLE BLACKLIST')
    cur.execute('DROP TABLE INACTIVE')
    cur.execute('DROP TABLE ACTIVE')
    conn.commit()
    cur.close()
    conn.close()
