import sqlite3

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
            print(product)
            product_id = int(input("ProductID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print(trans)
            trans_id = int(input("TransactionsID,int :"))
            check = True
        except ValueError:
            print("datatypr error")
            check = False
    transactions_product = (trans_id,product_id)
    insert_transactionsproduct_data(transactions_product)

if __name__ == "__main__":
    insert_transactionsproduct_main()
    
