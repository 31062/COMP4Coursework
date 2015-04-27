import sqlite3

def edit_deliverystock_data(data,field):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql_1 = """update DeliveryStock set
            DeliveryID = ?
            where DeliveryStockID = ?"""
        sql_2 = """update DeliveryStock set
            StockID = ?
            where DeliveryStockID = ?"""
        if field == 1:
            cursor.execute(sql_1,data)
        if field == 2:
            cursor.execute(sql_2,data)
        db.commit()


def edit_deliverystock_display():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select DeliveryStockID,DeliveryID,StockID from DeliveryStock")
        ds = cursor.fetchall()
    print("""please first enter the ID number of the row you wish to edit
then select which field you whish to edit or edit all fields at once,
finaly enter the new value for the field.""")
    print()
    print('{0:<6}{1:<10}{2:>12}'.format('ID','Delivery ID','stock ID'))
    for each1 in ds:
        print('{0:<6}{1:<10}{2:>6}'.format(each1[0],each1[1],each1[2]))
    print("")
    print("1. DeliveryID")
    print("2. StockID")
    print("")

def edit_deliverystock_input():
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

def edit_deliverystock_main():
    edit_deliverystock_display()
    field, data = edit_deliverystock_input()
    edit_deliverystock_data(data,field)

if __name__=="__main__":
    edit_deliverystock_main()
    
