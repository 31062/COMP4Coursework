import sqlite3

def create_stock_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Stock(
            StockID integer,
            PuchaseUnit text,
            PuchaseCost integer,
            ShelfLife text,
            DisplayQuantity integer,
            QuantityOfStockDisplayed integer,
            BrandID integer,
            SupplierID integer,
            primary key(StockID)
            foreign key(BrandID) references Brand(BrandID)
            foreign key(SupplierID) references Supplier(SupplierID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
