import sqlite3

def create_stockcheck_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table StockCheck(
            StockCheckID integer,
            StockCheckDate text
            NextStockCheckDate text,
            QuantityFound integer,
            UserID integer,
            StockID integer,
            primary key(StockCheckID)
            foreign key(UserID) references User(UserID)
            foreign key(StockID) references Stock(StockID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
