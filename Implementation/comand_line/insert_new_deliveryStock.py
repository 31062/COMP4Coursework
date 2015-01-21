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
    check = False
    while not check:
        try:
            deliveryID = int(input("deliveryID: "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            stockID = int(input("stockID: "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    d_stock = (deliveryID,stockID)
    insert_deliverystock_data(d_stock)    

if __name__ == "__main__":
    insert_deliverystock_main()
    
