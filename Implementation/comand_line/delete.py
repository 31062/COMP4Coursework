import sqlite3

def delete_user(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from User where UserID = ?"""
        cursor.execute(sql,data)
        db.commit()

def delete_brand(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Brand where BrandID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_delivery(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Delivery where DeliveryID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_location(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Location where LocationID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_supplier(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Supplier where SupplierID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_transactions(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Transactions where TransactionsID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_producttype(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Producttype where ProducttypeID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_stock(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Stock where StockID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_deliverystock(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from DeliveryStock where DeliveryStockID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_stockcheck(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from StockCheck where StockCheckID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_product(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from Product where ProductID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_transactionsproduct(data):
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """delete from TransactionsProduct where TransactionsProductID = ?"""
        cursor.execute(sql,data)
        db.commit()
        
def delete_user_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from User"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        
def delete_brand_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Brand"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_delivery_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Delivery"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_location_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Location"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_supplier_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Supplier"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_transactions_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Transactions"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_producttype_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from ProductType"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_stock_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Stock"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_deliverystock_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from DeliveryStock"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_stockcheck_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from StockCheck"""
        cursor.execute(sql)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_product_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from Product"""
        cursor.execute(sql,data)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_transactionsproduct_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        sql = """select * from TransactionsProduct"""
        cursor.execute(sql,data)
        temp = cursor.fetchall()
        for each in temp:
            print(each)
        data = input("input:")
        return data
        
def delete_display_1():
    print("please enter the table you would like to delete from")
    print()
    print("1. Brand")
    print("2. Supplier")
    print("3. Delivery")
    print("4. Location")
    print("5. Product")
    print("6. ProductType")
    print("7. Stock")
    print("8. StockCheck")
    print("9. Transactions")
    print("10. User")
    print("11. DeliveryStock")
    print("12. TransactionsProduct")
    print()

def user_choice():
    check = True
    while check:
        try:
            user_input = int(input("input:"))
            if user_input in [1,2,3,4,5,6,7,8,9,10,11,12]:
                check = False
            else:
                check = True
                print("please enter a valid")
        except ValueError:
            print("incorrect datatype")
            check = True
    if user_input == 1:
        data = delete_brand_display()
        delete_brand(data)
    elif user_input == 2:
        data = delete_supplier_display()
        delete_supplier(data)
    elif user_input == 3:
        data = delete_delivery_display()
        delete_delivery(data)
    elif user_input == 4:
        data = delete_location_display()
        delete_location(data)
    elif user_input == 5:
        data = delete_product_display()
        delete_product(data)
    elif user_input == 6:
        data = delete_producttype_display()
        delete_producttype(data)
    elif user_input == 7:
        data = delete_stock_display()
        delete_stock(data)
    elif user_input == 8:
        data = delete_stockcheck_display()
        delete_stockcheck(data)
    elif user_input == 9:
        data = delete_transactions_display()
        delete_transactions(data)
    elif user_input == 10:
        data = delete_user_display()
        delete_user(data)
    elif user_input == 11:
        data = delete_deliverystock_display()
        delete_deliverystock(data)
    elif user_input == 12:
        data = delete_transactionsproduct_display()
        delete_transactionsproduct(data)
    
def delete_main():
    delete_display_1()
    user_choice()
    



