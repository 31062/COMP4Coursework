import sqlite3

def amend_user_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update StockCheck set
            StockCheckDate = ?
            where StockCheckID = ?"""
        sql_2 = """update StockCheck set
            QuantityFound = ?
            where StockCheckID = ?"""
        sql_3 = """update StockCheck set
            UserID = ?
            where StockCheckID = ?"""
        sql_4 = """update StockCheck set
            StockID = ?
            where StockCheckID = ?"""
        if field == 1:
            cursor.execute(sql_1,data)
        if field == 2:
            cursor.execute(sql_2,data)
        if field == 3:
            cursor.execute(sql_3,data)
        if field == 4:
            cursor.execute(sql_4,data)
        db.commit()


def display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
    print("")
    print("1. StockCheckDate")
    print("2. QuantityFound")
    print("3. UserID")
    print("4. StockID")
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
    
