import sqlite3

def amend_user_data(data,field):
    print("field:",field)
    print("data;",data)
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


def display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
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

def user_input():
    row_ID = input("row ID :")
    field = int(input("field to edit :"))
    value = input("new data :")
    data = (value,row_ID)
    return field, data 

if __name__ == "__main__":
    display()
    field, data = user_input()
    amend_user_data(data,field)
    
