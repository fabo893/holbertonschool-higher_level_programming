#!/usr/bin/python3
"""
    5-filter_cities
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id=states.id WHERE\
                states.name = %s", (argv[4],))
    query_rows = cur.fetchall()
    c_list = []
    for row in query_rows:
        c_list.append(row[0])
    print(", ".join(c_list))
    cur.close()
    conn.close()
