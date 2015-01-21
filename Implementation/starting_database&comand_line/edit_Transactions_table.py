import sqlite3

def edit_transactions_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update Transactions set
            TransactionsTimeDate = ?
            where TransactionsID = ?"""
        sql_2 = """update Transactions set
            UserID = ?
            where TransactionsID = ?"""
        if field == 1:
            cursor.execute(sql_1,data)
        if field == 2:
            cursor.execute(sql_2,data)
        db.commit()


def edit_transactions_display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
    print("")
    print("1. TransactionsTimeDate")
    print("2. UserID")
    print("")

def edit_transactions_input():
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

def edit_transactions_main():
    edit_transactions_display()
    field, data = edit_transactions_input()
    edit_transactions_data(data,field)

if __name__ == "__main__":
    edit_transactions_main()
    
    
