import sqlite3

def edit_delivery_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update Delivery set
            DeliveryTimeDate = ?
            where DeliveryID = ?"""
        cursor.execute(sql_1,data)
        db.commit()


def edit_delivery_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select DeliveryID,DeliveryTimeDate from Delivery")
        delivery = cursor.fetchall()
    print("""please first enter the ID number of the row you wish to edit
then select which field you whish to edit or edit all fields at once,
finaly enter the new value for the field.""")
    print()
    print('{0:<6}{1:<10}'.format('ID','Delivery Time Date'))
    for each1 in delivery:
        print('{0:<6}{1:<10}'.format(each1[0],each1[1]))
    print("")
    print("1. DeliveryTimeDate")
    print("")

def edit_delivery_input():
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

def edit_delivery_main():
    edit_delivery_display()
    field, data = edit_delivery_input()
    edit_delivery_data(data,field)

if __name__ == "__main__":
    edit_delivery_main()
    
