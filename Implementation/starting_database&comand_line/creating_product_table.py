import sqlite3

#open/create new database
with sqlite3.connect("pub_stock.db") as db:
    #make the cursor
    cursor = db.cursor()
    #create sql
    sql = """create table Product(
        ProductID integer,
        RetailPrice real,
        RetailUnit text,
        ProductName text,
        AlcoholPercentage real,
        ProductTypeID integer,
        LocationID integer,
        BrandID integer,
        StockID integer,
        primary key(ProductID)
        foreign key(ProductTypeID) references ProductType(ProductTypeID)
        foreign key(LocationID) references Location(LocationID)
        foreign key(BrandID) references Brand(BrandID)
        foreign key(StockID) references Stock(StockID))"""
    #execute sql code
    cursor.execute(sql)
    #commit to database
    db.commit()
