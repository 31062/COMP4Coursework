import sqlite3

def create_location_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Location(
            LocationID integer,
            LocationName text,
            primary key(LocationID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
