import sqlite3
def transaction_user():
    user_ID = input("please enter your userID")
    print()

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
    print("enter 0 when u have entered all the products")
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
        
        
    
def transaction_main():
    #transaction_user
    transaction_product()

if __name__=="__main__":
    transaction_main()
