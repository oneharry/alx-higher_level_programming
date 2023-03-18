#!/usr/bin/python3
""" Module prints all states in database"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    curr = conn.cursor()
    curr.execute("SLECT * FROM states ORDER BY states.id ASC")
    irows = curr.fetchall()
    for irow in irows:
        print(irow)
