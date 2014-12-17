import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Stock(PuchaseUnit,PuchaseCost,ShelfLife,DisplayQuantity,QuantityOfStockDisplayed,BrandID, SupplierID) values(?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    p_unit = input("puchase unit : ")
    p_cost = int(input("puchase cost : "))
    s_life = input("shelf life : ")
    d_quantity = int(input("display quantity : "))
    QOSD = int(input("quantity of stock displayedt : "))
    brandid = int(input("brandID : "))
    supplierid = int(input("supplierID : "))
    
    stock = (p_unit,p_cost,s_life,d_quantity,QOSD,brandid,supplierid)
    insert_data(stock)
