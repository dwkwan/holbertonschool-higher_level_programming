#!/usr/bin/python3
"""This module contains a script that lists all cities of a passed state"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities" +
    " INNER JOIN states ON cities.state_id = states.id " +
    " WHERE states.name = %s" + " ORDER BY" + " cities.id ASC"
    cur.execute(query, [sys.argv[4]])
    query_rows = cur.fetchall()
    for row in range(len(query_rows) - 1):
        print("{}, ".format(query_rows[row][0]), end="")
    print(query_rows[len(query_rows) - 1][0])
    cur.close()
    conn.close()
