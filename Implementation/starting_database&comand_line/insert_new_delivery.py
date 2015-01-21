import sqlite3

def insert_delivery_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Delivery(DeliveryTimeDate) values(?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_delivery_main():
    time = input("delivery time date : ")
    delivery = (time,)
    insert_delivery_data(delivery)

if __name__ == "__main__":
    insert_delivery_main()
    
