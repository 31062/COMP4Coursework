import sqlite3

def delete_user(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from User where UserID = ?"""

def delete_brand(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Brand where BrandID = ?"""

def delete_delivery(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Delivery where DeliveryID = ?"""

def delete_location(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Location where LocationID = ?"""

def delete_supplier(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Supplier where SupplierID = ?"""

def delete_transactions(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Transactions where TransactionsID = ?"""

def delete_producttype(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Producttype where ProducttypeID = ?"""

def delete_stock(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Stock where StockID = ?"""

def delete_deliverystock(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from DeliveryStock where DeliveryStockID = ?"""

def delete_stockcheck(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from StockCheck where StockCheckID = ?"""

def delete_product(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from Product where ProductID = ?"""

def delete_transactionsproduct(data):
    while sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor
        sql = """delete from TransactionsProduct where TransactionsProductID = ?"""

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

def delete_display_2():

def user_choice():
    check = True
    while check:
        try:
            user_input = int(input())
            if user_input is in [1,2,3,4,5,6,7,8,9,10,11,12]:
                check = False
            else:
                check = True
                print("please enter a valid
        except ValueError:
            print("incorrect datatype")
            check = True

def delete_main():
    delete_display_1()
    user_choice()


