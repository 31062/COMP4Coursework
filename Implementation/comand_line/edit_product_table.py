import sqlite3

def edit_product_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update Product 
            set RetailPrice = ?
            where ProductID = ?"""
        sql_2 = """update Product set
            RetailPrice = ?
            where ProductID = ?"""
        sql_3 = """update Product set
            ProductName = ?
            where ProductID = ?"""
        sql_4 = """update Product set
            AlcoholPercentage = ?
            where ProductID = ?"""
        sql_5 = """update Product set
            ProductTypeID = ?
            where ProductID = ?"""
        sql_6 = """update Product set
            LocationID = ?
            where ProductID = ?"""
        sql_7 = """update Product set
            BrandID = ?
            where ProductID = ?"""
        sql_8 = """update Product set
            StockID = ?
            where productID = ?"""
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
        if field == 8:
            cursor.execute(sql_8,data)
        db.commit()


def edit_product_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select ProductID,RetailPrice,RetailUnit,ProductName,AlcoholPercentage,ProductTypeID,LocationID,BrandID,StockID from Product")
        product = cursor.fetchall()
    print("""please first enter the ID number of the row you wish to edit
then select which field you whish to edit or edit all fields at once,
finaly enter the new value for the field.""")
    print()
    print('{0:<6}{1:<10}'.format('ID','RetailPrice','RetailUnit','ProductName','AlcoholPercentage','ProductTypeID','LocationID','BrandID','StockID'))
    for each1 in product:
        print('{0:<6}{1:<10}'.format(each1[0],each1[1]))
    print("")
    print("1. RetailPrice")
    print("2. RetailUnit")
    print("3. ProductName")
    print("4. AlcoholPercentage")
    print("5. ProductTypeID")
    print("6. LocationID")
    print("7. BrandID")
    print("8. StockID")
    print("")

def edit_product_input():
    check = False
    while not check:
        try:
            row_ID = int(input("row ID,str :"))
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

def edit_product_main():
    edit_product_display()
    field, data = edit_product_input()
    edit_product_data(data,field)
    
if __name__ == "__main__":
    edit_product_main()
    
    
