#!/usr/bin/python3
"""
    2-my_filter_states
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    arg = argv[4]
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY\
                id ASC".format(arg))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
