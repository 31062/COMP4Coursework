import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into DeliveryStock(DeliveryID,StockID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    deliveryID = int(input("deliveryID : "))
    stockID = int(input("stockID : "))
    
    
    d_stock = (deliveryID,stockID)
    insert_data(d_stock)
