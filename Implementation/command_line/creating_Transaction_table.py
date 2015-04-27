import sqlite3

def create_transactions_table():
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """create table Transactions(
            TransactionsID integer,
            TransactionsTimeDate text,
            UserID integer,
            primary key(TransactionsID),
            foreign key(UserID) references User(UserID))"""
        #execute sql code
        cursor.execute(sql)
        #commit to database
        db.commit()
