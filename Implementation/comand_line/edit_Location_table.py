import sqlite3

def edit_location_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update Location 
            set LocationName = ?
            where LocationID = ?"""
        cursor.execute(sql_1,data)
        db.commit()


def edit_location_display():
    print("""please first enter the ID number of the row you wish to edit
        then select which field you whish to edit or edit all fields at once, finaly enter the new value
        for the field""")
    print("")
    print("1. LocationName")
    print("")

def edit_location_input():
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

def edit_location_main():
    edit_location_display()
    field, data = edit_location_input()
    edit_location_data(data,field)

if __name__ == "__main__":
    edit_location_main()
    
