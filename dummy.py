import psycopg2

ADMIN_PASSWORD = '48c5ae'

UID = ['26e1a2', '54gdg5', 'y67tu7', 'e4r45r', '7ui87h', 'ty6er6']
HASHES = ['$2b$12$ldy3v6k0TLT3cBT8UQmEAO6WZiJ3xHarDKuA8cbCcy4UgpCvyVaku',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e',
          '$2b$12$/dGzsj9pYPWmhcTlzVC83uy916PKH9dWjl6SMy.S97p4BvoGIdU3e'
          ]
NAMES = ['Admin', 'Jignesh Kumar', 'Akash Kumar', 'Subodh Chaurasiya', 'Meena Kumari', 'Kulbhushan Singh']
TIME = ['2019-06-16 17:34:35.000000', '2019-06-20 12:21:34.000000', '2019-06-20 12:21:59.000000',
        '2019-06-20 12:22:49.000000', '2019-06-20 12:23:34.000000', '2019-06-20 12:24:24.000000']


def create_dummy_data():
    conn = psycopg2.connect(dbname='themilkyway', user='postgres', password='1999')
    cur = conn.cursor()
    for i in range(6):
        cur.execute('INSERT INTO active (uid, time, name, email, password) VALUES (%s, %s, %s, %s, %s)',
                    (UID[i], TIME[i], NAMES[i], ('.'.join(NAMES[i].split()) + '@gmail.com'), HASHES[i]))
    conn.commit()
    cur.close()
    conn.close()
