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
    check = False
    while not check:
        try:
            product_id = int(input("ProductID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            trans_id = int(input("TransactionsID,int :"))
            check = True
        except ValueError:
            print("datatypr error")
            check = False
    transactions_product = (trans_id,product_id)
    insert_transactionsproduct_data(transactions_product)

if __name__ == "__main__":
    insert_transactionsproduct_main()
    
