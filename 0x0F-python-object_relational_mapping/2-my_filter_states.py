#!/usr/bin/python3
""" Module prints all states in database
    Takes an argument, and returns all values
    where name matches argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    curr = conn.cursor()
    curr.execute("SELECT * FROM states\
                 WHERE BINARY name = '{}'".format(arg[4]))
    for i in curr.fetchall():
        print(i)
