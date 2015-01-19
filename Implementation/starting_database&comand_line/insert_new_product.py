import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Product(RetailPrice,RetailUnit,ProductName,AlcoholPercentage,ProductTypeID,locationID,BrandID,StockID) values(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    r_price = float(input("retail price,float :"))
    r_unit = int(input("retail unit,int :")) 
    product_name = input("product name,str :") 
    AP = float(input("Alcohol Percentage,float :")) 
    product_typeID = int(input("product_typeID,int :"))  
    locationID = int(input("locationID,int :"))
    brandID = int(input("brandID,int :"))
    stockID = int(input("stockID,int :"))
    check = isinstance(stockID,int)
    product = (r_price,r_unit,product_name,product_typeID,AP,locationID,brandID,stockID)
    insert_data(product)
