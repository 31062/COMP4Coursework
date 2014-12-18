import sqlite3

def amend_user_first_name(data):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """update User set
            UserFirstName = ?
            where UserID = ?"""
        cursor.execute(sql,data)
        db.commit()


def display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit, finaly enter the new value
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

def user_input():
    row_ID = input("row ID :")
    field = input("field to edit :")
    value = input("new data :")
    data = (value,row_ID)
    print(data)
    return field, data 

def execute_user_choice(field):
    if field == 1:
        print()
        print(data)
        amend_user_first_name(data)
    
        
    


if __name__ == "__main__":
    display()
    field, data = user_input()
    execute_user_choice(field)
    
