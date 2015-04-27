import sqlite3

def edit_stock_data(data, field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update Stock set
            PuchaseUnit = ?
            where StockID = ?"""
        sql_2 = """update Stock set
            PuchaseCost = ?
            where StockID = ?"""
        sql_3 = """update Stock set
            ShelfLife = ?
            where StockID = ?"""
        sql_4 = """update Stock set
            DisplayQuantity = ?
            where StockID = ?"""
        sql_5 = """update Stock set
            QuantityOfStockDisplayed = ?
            where StockID = ?"""
        sql_6 = """update Stock set
            BrandID = ?
            where StockID = ?"""
        sql_7 = """update Stock set
            SupplierID = ?
            where StockID = ?"""
        if field == 1:
            cursor.execute(sql_1,data)
        if field == 2:
            cursor.execute(sql_2,data)
        if field == 3:
            cursor.execute(sql_3,data)
        if field == 4:
            cursor.execute(sql_4,data)
        if field == 5:
            cursor.execute(sql_5,data)
        if field == 6:
            cursor.execute(sql_6,data)
        if field == 7:
            cursor.execute(sql_7,data)
        db.commit()


def edit_stock_display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
    print("")
    print("1. PuchaseUnit")
    print("2. puchaseCost")
    print("3. ShelfLife")
    print("4. DisplayQuantity")
    print("5. QuantityOfStockDisplayed")
    print("6. BrandID")
    print("7. SupplierID")
    print("")

def edit_stock_input():
    check = False
    while not check:
        try:
            row_ID = int(input("row ID :"))
            check = True
        except ValueError:
            print("invalid data type")
            check = False
    check = False
    while not check:
        try:
            field = int(input("field to edit :"))
            check = True
        except ValueError:
            print("invalid data type")
            check = False
    value = input("new data :")     
    data = (value,row_ID)
    return field, data

def edit_stock_main():
    edit_stock_display()
    field, data = edit_stock_input()
    edit_stock_data(data,field)

if __name__ == "__main__":
    edit_stock_main()
    
    
