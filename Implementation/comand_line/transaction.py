import sqlite3
import datetime
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
        sql = """select ProductID,ProductName,RetailPrice from Product """
        cursor.execute(sql)
        product = cursor.fetchall()
    print("ID   product name   price")
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
    return productID_list, product

def transaction_insert_transaction(user_ID):
    time_stamp = datetime.datetime.now()
    values = (time_stamp,user_ID)
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """insert into Transactions(TransactionsTimeDate,UserID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()
    
def transaction_insert_transactionproduct(productID_list):
    with sqlite3.connect("pub_stock.db") as db:
            cursor = db.cursor()
            cursor.execute("select max(TransactionsID) from transactions")
            transaction_id = cursor.fetchall()
            transaction_id = (transaction_id[0])
    check = True
    point = len(productID_list)
    pointer = 0
    for count in productID_list:
        product_ID = productID_list[pointer]
        values = (product_ID,transaction_id[0])
        with sqlite3.connect("pub_stock.db") as db:
            cursor = db.cursor()
            sql = """insert into TransactionsProduct(ProductID,TransactionsID) values(?,?)"""
            cursor.execute(sql,values)
            db.commit()
        pointer += 1

def payment(product,productID_list):
    b_products_list = []
    price_list = product[2]
    count = 0
    for each in productID_list:
        value = productID_list[count]
        count += 1
        temp = product[value-1][2]
        b_products_list.append(temp)
    cost = 0
    for each1 in b_products_list:
        print(cost)
        print(b_products_list[each1-1])
        cost += b_products_list[each1-1] 
        
    
def transaction_main():
    print("----TRANSACTION----")
    user_ID = transaction_user()
    productID_list, product = transaction_product()
    payment(product,productID_list)
    transaction_insert_transaction(user_ID)
    transaction_insert_transactionproduct(productID_list)
    print("----TRANSACTION_COMPLETE----")

if __name__=="__main__":
    transaction_main()
