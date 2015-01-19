import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into TransactionsProduct(ProductID,TransactionsID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    product_id = int(input("ProductID,int :"))
    trans_id = int(input("TransactionsID,int :"))
    transactions_product = (trans_id,product_id)
    insert_data(transactions_product)
