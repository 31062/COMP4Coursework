import sqlite3

def edit_transactionsproduct_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update TransactionsProduct set
            ProductID = ?
            where TransactionsProductID = ?"""
        sql_2 = """update TransactionsProduct set
            TransactionsID = ?
            where TransactionsProductID = ?"""
        if field == 1:
            cursor.execute(sql_1,data)
        if field == 2:
            cursor.execute(sql_2,data)
        db.commit()


def edit_transactionsproduct_display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
    print("")
    print("1. ProductID")
    print("2. TransactionsID")
    print("")

def edit_transactionsproduct_input():
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

def edit_transactionsproduct_main():
    edit_transactionsproduct_display()
    field, data = edit_transactionsproduct_input()
    edit_transactionsproduct_data(data,field)

if __name__ == "__main__":
    edit_transactionsproduct_main()
    
    
