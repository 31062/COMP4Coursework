import sqlite3

#open/create new database
with sqlite3.connect("pub_stock.db") as db:
    #make the cursor
    cursor = db.cursor()
    #create sql
    sql = """create table ProductType(
        ProductTypeID integer,
        TypeName text,
        primary key(ProductTypeID))"""
    #execute sql code
    cursor.execute(sql)
    #commit to database
    db.commit()
