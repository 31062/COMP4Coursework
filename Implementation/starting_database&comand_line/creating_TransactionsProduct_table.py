import sqlite3

#open/create new database
with sqlite3.connect("pub_stock.db") as db:
    #make the cursor
    cursor = db.cursor()
    #create sql
    sql = """create table TransactionsProduct(
        TransactionsProductID integer,
        ProductID integer,
        TransactionsID integer,
        primary key(TransactionsProductID),
        foreign key(TransactionsID) references Transactions(TransactionsID),
        foreign key(ProductID) references Product(ProductID))"""
    #execute sql code
    cursor.execute(sql)
    #commit to database
    db.commit()
