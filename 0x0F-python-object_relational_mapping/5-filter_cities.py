#!/usr/bin/python3
""" Module takes in name as argument and lists all
    cities of that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(user=arg[1], passwd=arg[2], db=arg[3])
    curr = conn.cursor()
    curr.execute("SELECT *\
                 FROM cities\
                 INNER JOIN states\
                 ON cities.state_id = states.id\
                 ORDER BY cities.id")
    my_list = []
    for i in curr.fetchall():
        if (i[4] == arg[4]):
            my_list.append(i[2])
    print(", ".join(my_list))
