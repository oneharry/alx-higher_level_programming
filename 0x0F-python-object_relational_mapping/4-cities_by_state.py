#!/usr/bin/python3
""" Module prints all cities in database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    curr = conn.cursor()
    curr.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities\
                 INNER JOIN states\
                 ON cities.state_id = states.id\
                 ORDER BY cities.id")
    for i in curr.fetchall():
        print(i)
