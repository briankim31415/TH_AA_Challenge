import sqlite3

import random
from datetime import datetime

conn = sqlite3.connect('rr.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE rrline (passenger_id, passenger_name, time)''')
except:
    pass
# conn.commit()
# c.execute('''INSERT INTO rrline values('2', 'Jeemin Han', '12:34')''')
# conn.commit()

# t = ('2')
# c.execute('DELETE FROM rrline where passenger_id=?' ,t)

# c.execute('SELECT length(time) FROM rrline')

# print(int(str(c.fetchone()).split(',')[0].lstrip('(')))

def add_to_list(passenger):
    passenger = passenger.replace(' ','_')
    ran = random.randint(5321,12359)
    curr_time = str(datetime.now())[11:16]
    c.execute('INSERT INTO rrline values(?,?,?)',(ran, passenger, curr_time))
    conn.commit()
    print('INSERT INTO rrline values(?,?,?)',(ran, passenger, curr_time))

def remove_from_list(id):
    id = str(id)
    c.execute('DELETE FROM rrline where passenger_id=(?)',[id])
    conn.commit()

def query():
    c.execute('SELECT length(time) FROM rrline')
    print(c.fetchall())
    return((int(str(c.fetchone()).split(',')[0].lstrip('('))))

c.close()
    