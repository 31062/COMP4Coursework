import sqlite3

def create_supplier_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Supplier(
            SupplierID integer,
            SupplierName text,
            primary key(SupplierID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
