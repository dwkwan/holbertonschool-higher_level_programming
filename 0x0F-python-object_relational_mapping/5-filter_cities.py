#!/usr/bin/python3
"""This module contains a script that lists all cities of a passed state"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT cities.name FROM cities"
    query = query + " INNER JOIN states ON cities.state_id = states.id"
    query = query + " WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, [sys.argv[4]])
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
