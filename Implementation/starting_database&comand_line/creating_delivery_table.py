import sqlite3

def create_delivery_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Delivery(
            DeliveryID integer,
            DeliveryTimeDate text,
            primary key(DeliveryID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
