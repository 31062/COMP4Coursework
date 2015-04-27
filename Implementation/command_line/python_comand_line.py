import sqlite3
from edit_brand_table import *
from edit_Delivery_table import *
from edit_DeliveryStock_table import *
from edit_Location_table import *
from edit_product_table import *
from edit_ProductType_table import *
from edit_stock_table import *
from edit_StockCheck_table import *
from edit_Supplier_table import *
from edit_Transactions_table import *
from edit_TransactionsProduct_table import *
from edit_user_table import *
from insert_new_brand import *
from insert_new_delivery import *
from insert_new_deliveryStock import *
from insert_new_location import *
from insert_new_product import *
from insert_new_productType import *

from insert_new_Stock import *
from insert_new_stockCheck import *
from insert_new_supplier import *
from insert_new_Transactions import *
from insert_new_Transactionsproduct import *
from insert_new_user import *
from creating_brand_table import *
from creating_delivery_table import *
from creating_DeliveryStock_table import *
from creating_location_table import *
from creating_product_table import *
from creating_ProductType_table import *
from creating_stock_table import *
from creating_StockCheck_table import *
from creating_supplier_table import *
from creating_Transaction_table import *
from creating_TransactionsProduct_table import *
from creating_user_table import *
from transaction import *
from delete import *

def comand_display_1():
    print()
    print("select what you wish to do")
    print()
    print("1. Create new database.")
    print("2. Insert a new line in a database table.")
    print("3. Edit a currenlty exsisting line in the database.")
    print("4. Make transaction.")
    print("5. Delete line from database.")
    print("0. Exit program.")
    print()

def comand_display_2():
    print()
    print("select the table in which u which to insert data.")
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

def display_2_input():
    print()
    check = False
    while not check:
        try:
            display_2_choice = int(input("input :"))
            if display_2_choice in [1,2,3,4,5,6,7,8,9,10,11,12]:
                check = True
            else:
                print("index of of range")
                check = False
        except ValueError:
            print("datatype error")
            check = False
    print()
    return display_2_choice

def display_1_input():
    print()
    check = False
    while not check:
        try:
            display_1_choice = int(input("input :"))
            if display_1_choice in [0,1,2,3,4,5]:
                check = True
            else:
                print("index out of range")
                check = False
        except ValueError:
            print("datatype error")
            check = False
    print() 
    return display_1_choice

def insert_database(display_2_choice):
    if display_2_choice == 1:
        insert_brand_main()
    if display_2_choice == 2:
        insert_supplier_main()
    if display_2_choice == 3:
        insert_delivery_main()
    if display_2_choice == 4:
        insert_location_main()
    if display_2_choice == 5:
        insert_product_main()
    if display_2_choice == 6:
        insert_producttype_main()
    if display_2_choice == 7:
        insert_stock_main()
    if display_2_choice == 8:
        insert_stockcheck_main()
    if display_2_choice == 9:
        insert_transactions_main()
    if display_2_choice == 10:
        insert_user_main()
    if display_2_choice == 11:
        insert_deliverystock_main()
    if display_2_choice == 12:
        insert_transactionsproduct_main()

def edit_database(display_2_choice):
    if display_2_choice == 1:
        edit_brand_main()
    if display_2_choice == 2:
        edit_supplier_main()
    if display_2_choice == 3:
        edit_delivery_main()
    if display_2_choice == 4:
        edit_location_main()
    if display_2_choice == 5:
        edit_product_main()
    if display_2_choice == 6:
        edit_producttype_main()
    if display_2_choice == 7:
        edit_stock_main()
    if display_2_choice == 8:
        edit_stockcheck_main()
    if display_2_choice == 9:
        edit_transactions_main()
    if display_2_choice == 10:
        edit_user_main()
    if display_2_choice == 11:
        edit_deliverystock_main()
    if display_2_choice == 12:
        edit_transactionsproduct_main()

        
    

def create_database():
    create_user_table()
    create_brand_table()
    create_delivery_table()
    create_location_table()
    create_supplier_table()
    create_transactions_table()
    create_producttype_table()
    create_stock_table()
    create_deliverystock_table()
    create_stockcheck_table()
    create_product_table()
    create_transactionsproduct_table()
    
def end_program():
    quit()
    
def comand_main():
    comand_display_1()
    display_1_choice = display_1_input()
    if display_1_choice == 1:
        create_database()
        print("your data base has been created and named:pub_stock")
    if display_1_choice == 3:
        comand_display_2()
        display_2_choice = display_2_input()
        edit_database(display_2_choice)
    if display_1_choice == 2:
        comand_display_2()
        display_2_choice = display_2_input()
        insert_database(display_2_choice)
    if display_1_choice == 0:
        end_program()
    if display_1_choice == 4:
        transaction_main()
    if display_1_choice == 5:
        delete_main()

if __name__=="__main__":
    repeat = True
    while repeat:
        comand_main() 
    
















    
    
