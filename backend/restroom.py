import sqlite3

conn = sqlite3.connect('rr.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE rrline (passenger_id, passenger_name, time)''')
except:
    pass
conn.commit()
c.execute('''INSERT INTO rrline values('2', 'Jeemin Han', '12:34')''')
conn.commit()

# t = ('2')
# c.execute('DELETE FROM rrline where passenger_id=?' ,t)

c.execute('SELECT length(time) FROM rrline')

print(int(str(c.fetchone()).split(',')[0].lstrip('(')))