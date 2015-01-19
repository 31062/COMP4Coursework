import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Stock(PuchaseUnit,PuchaseCost,ShelfLife,DisplayQuantity,QuantityOfStockDisplayed,BrandID,SupplierID) values(?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    p_unit = input("PuchaseUnit,str :")
    p_cost = float(input("PuchaseCost,float :"))
    SL = input("ShelfLife,str :")
    dis_quan = int(input("DisplayQuantity,int :"))
    quan_of_stock_dis = int(input("QuantityOfStockDisplayed,int :"))
    brandID = int(input("BrandID,int :"))
    supplierID = int(input("SupplierID,int :"))
    check = isinstance(supplierID,int)
    product = (p_unit,p_cost,SL,dis_quan,quan_of_stock_dis,brandID,supplierID)
    insert_data(product)
