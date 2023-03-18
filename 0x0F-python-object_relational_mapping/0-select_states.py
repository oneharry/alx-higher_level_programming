#!/usr/bin/python3
""" Module prints all states in database"""

import sys
import MySQLdb

arg = sys.argv
conn = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                       passwd=arg[2], db=arg[3], charset="utf8")
curr = conn.cursor()
curr.execute("SLECT * FROM states ORDER BY states.id ASC")
rows = curr.fetchall()
for row in rows:
    print(row)
curr.close()
conn.close()
