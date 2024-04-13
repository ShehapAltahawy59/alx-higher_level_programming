
#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

if __name__  == "__main__":
    import MySQLdb
    import sys
    MY_USER= sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host="localhost",port=3306, user=MY_USER, passwd=MY_PASS, db=MY_DB)
    cur = db.cursor()
    cur.execute("SELECT *  FROM states ORDERD BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows :
        print(row)
    