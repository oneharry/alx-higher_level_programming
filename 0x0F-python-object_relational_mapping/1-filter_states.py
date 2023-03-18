#!/usr/bin/python3
""" Module prints all states in database
    with names starting with N
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    curr = conn.cursor()
    curr.execute("SELECT * FROM states WHERE states.name LIKE 'N%'")
    for i in curr.fetchall():
        print(i)
