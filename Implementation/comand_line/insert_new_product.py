import sqlite3

def insert_product_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Product(RetailPrice,RetailUnit,ProductName,AlcoholPercentage,ProductTypeID,locationID,BrandID,StockID) values(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_product_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select ProductTypeID,TypeName from ProductType")
        producttype = cursor.fetchall()
        cursor.execute("select LocationID,LocationName from Location")
        location = cursor.fetchall()
        cursor.execute("select BrandID,BrandName from Brand")
        brand = cursor.fetchall()
        cursor.execute("select StockID from Stock")
        stock = cursor.fetchall()
        
    check = False
    while not check:
        try:
            r_price = float(input("retail price,float :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    r_unit = input("retail unit,str :")
    product_name = input("product name,str :")
    check = False
    while not check:
        try:
            AP = float(input("Alcohol Percentage,float :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print(producttype)
            product_typeID = int(input("product_typeID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print(location)
            locationID = int(input("locationID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print(brand)
            brandID = int(input("brandID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print(stock)
            stockID = int(input("stockID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    product = (r_price,r_unit,product_name,product_typeID,AP,locationID,brandID,stockID)
    insert_product_data(product)

if __name__ == "__main__":
    insert_product_main()
    
