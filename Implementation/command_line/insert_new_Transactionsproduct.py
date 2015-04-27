import sqlite3
import datetime

def insert_transactionsproduct_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into TransactionsProduct(ProductID,TransactionsID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_transactionsproduct_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select ProductID,ProductName from Product")
        product = cursor.fetchall()
        cursor.execute("select TransactionsID,TransactionsTimeDate,UserID from Transactions")
        trans = cursor.fetchall()
    check = False
    while not check:
        try:
            print("{0:<6}".format("ID"))
            for each1 in product:
                print("{0:<6}".format(each1[0]))
            print()
            product_id = int(input("ProductID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print("{0:<6}".format("ID"))
            for each in trans:
                print("{0:<6}".format(each[0]))
            print()
            trans_id = int(input("TransactionsID,int :"))
            check = True
        except ValueError:
            print("datatypr error")
            check = False
    transactions_product = (trans_id,product_id)
    insert_transactionsproduct_data(transactions_product)

if __name__ == "__main__":
    insert_transactionsproduct_main()
    
