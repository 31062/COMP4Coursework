import sqlite3
def transaction_user():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select UserID,UserFirstName,UserLastName from User")
        user = cursor.fetchall()
    print("ID  firstname  lastname")
    for each in user:
        print(each)
    user_ID = input("Please enter your userID.")
    print()
    return user_ID

def transaction_product():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select ProductID,ProductName from Product """
        cursor.execute(sql)
        product = cursor.fetchall()
    print("ID   product name")
    for each in product:
        print(each)
    print()
    productID_list = []
    print("Enter 0 when you have entered all the products for this transaction.")
    check_2 = True
    while check_2:
        try:
            productID = int(input("ProductID :"))
            if productID == 0:
                check_2 = False
            else:
                productID_list.append(productID)
                check_2 = True
        except ValueError:
            print("datatype error")
            check_2 = True

def transaction_insert_transaction(user_ID):
    ts = datetime.datetime.now()
    print(ts)
    values = (time_stamp,user_ID)
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """insert into Transactions(TransactionsTimeDateID,UserID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()
    
def transaction_insert_transactionproduct():
    with sqlite3.connect("pub_stock.db") as db:
            cursor = db.cursor()
            cursor.execute("select TransactionsID from Transactions order desc")
            cursor.execute("select TransactionsID from transactions")
            transaction_id = cursor.fetchone()
    for each in productID_list:
        values = (productID_list[each],transaction_id)
        with sqlite3.connect("pub_stock.db") as db:
            cursor = db.cursor()
            sql = """insert into TransactionsProduct(ProductID,TransactionsID) values(?,?)"""
            cursor.execute(sql,values)
            db.commit()
    
def transaction_main():
    print("----TRANSACTION----")
    user_ID = transaction_user()
    transaction_product()
    transaction_insert_transaction(user_ID)
    transaction_insert_transactionproduct()
    print("----TRANSACTION_COMPLETE----")

if __name__=="__main__":
    transaction_main()
