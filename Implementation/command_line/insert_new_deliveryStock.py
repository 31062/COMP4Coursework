import sqlite3

def insert_deliverystock_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into DeliveryStock(DeliveryID,StockID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_deliverystock_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select DeliveryID,DeliveryTimeDate from Delivery")
        delivery = cursor.fetchall()
        cursor.execute("select StockID from Stock")
        stock = cursor.fetchall()
    check = False
    while not check:
        try:
            print("{0:<6}".format("ID"))
            for each in delivery:
                print("{0:<6}".format(each[0]))
            print()
            deliveryID = int(input("deliveryID: "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print()
            print("{0:<6}".format("ID"))
            for each_1 in stock:
                print("{0:<6}".format(each_1[0]))
            print()
            stockID = int(input("stockID: "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    d_stock = (deliveryID,stockID)
    insert_deliverystock_data(d_stock)    

if __name__ == "__main__":
    insert_deliverystock_main()
    
