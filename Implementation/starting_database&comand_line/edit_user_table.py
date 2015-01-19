import sqlite3

def amend_user_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update User 
            set UserFirstName = ?
            where UserID = ?"""
        sql_2 = """update User set
            UserLastNme = ?
            where UserID = ?"""
        sql_3 = """update User set
            UserPhoneNumber = ?
            where UserID = ?"""
        sql_4 = """update User set
            UserEmailAddress = ?
            where UserID = ?"""
        sql_5 = """update User set
            UserCity = ?
            where UserID = ?"""
        sql_6 = """update User set
            UserStreet = ?
            where UserID = ?"""
        sql_7 = """update User set
            UserHouseNumber = ?
            where UserID = ?"""
        sql_8 = """update User set
            UserPostcode = ?
            where UserID = ?"""
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
    print("1. UserFirstName")
    print("2. UserLastNme")
    print("3. UserPhoneNumber")
    print("4. UserEmailAddress")
    print("5. UserCity")
    print("6. UserStreet")
    print("7. UserHouseNumber")
    print("8. UserPostcode")
    print("")

def def user_input():
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

if __name__ == "__main__":
    display()
    field, data = user_input()
    amend_user_data(data,field)
    
