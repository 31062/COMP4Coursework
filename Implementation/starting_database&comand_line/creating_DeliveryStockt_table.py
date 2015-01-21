import sqlite3

def create_deliverystock_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table DeliveryStock(
            DeliveryStockID integer,
            DeliveryID integer,
            StockID integer,
            primary key(DeliveryStockID)
            foreign key(DeliveryID) references Delivery(DeliveryID)
            foreign key(StockID) references Stock(StockID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
