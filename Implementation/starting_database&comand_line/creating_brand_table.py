import sqlite3
def create_brand_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Brand(
            BrandID integer,
            BrandName text,
            primary key(BrandID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
