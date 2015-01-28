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
            print()
            print("{0:<6}{1:<10}".format("ID", "type name"))
            for each_1 in producttype:
                print("{0:<6}{1:<10}".format(each_1[0], each_1[1]))
            print()
            product_typeID = int(input("product_typeID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print()
            print("{0:<6}{1:<10}".format("ID", "location name"))
            for each_2 in location:
                print("{0:<6}{1:<10}".format(each_2[0], each_2[1]))
            print()
            locationID = int(input("locationID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print()
            print("{0:<6}{1:<10}".format("ID", "brand name"))
            for each_3 in brand:
                print("{0:<6}{1:<10}".format(each_3[0], each_3[1]))
            print()
            brandID = int(input("brandID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print()
            print("{0:<6}".format("ID"))
            for each_4 in stock:
                print("{0:<6}".format(each_4[0]))
            print()
            stockID = int(input("stockID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    product = (r_price,r_unit,product_name,product_typeID,AP,locationID,brandID,stockID)
    insert_product_data(product)

if __name__ == "__main__":
    insert_product_main()
    
