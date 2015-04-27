import sqlite3

def insert_stock_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Stock(PuchaseUnit,PuchaseCost,ShelfLife,DisplayQuantity,QuantityOfStockDisplayed,BrandID,SupplierID) values(?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_stock_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select BrandID,BrandName from Brand")
        brand = cursor.fetchall()
        cursor.execute("select SupplierID,SupplierID from Supplier")
        supplier = cursor.fetchall()
    p_unit = input("PuchaseUnit,str :")
    check = False
    while not check:
        try:
            p_cost = int(input("PuchaseCost,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    SL = input("ShelfLife,str :")
    check = False
    while not check:
        try:
            dis_quan = int(input("DisplayQuantity,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            quan_of_stock_dis = int(input("QuantityOfStockDisplayed,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print('{0:<6}{1:<10}'.format('ID','brand name'))
            for each1 in brand:
                print('{0:<6}{1:<10}'.format(each1[0],each1[1]))
            print()
            brandID = int(input("BrandID,int :"))
            print()
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            print('{0:<6}{1:<10}'.format('ID','supplier name'))
            for each2 in supplier:
                print('{0:<6}{1:<10}'.format(each1[0],each1[1]))
            print()
            supplierID = int(input("SupplierID,int :"))
            print()
            check = True
        except ValueError:
            print("datatype error")
            check = False
    product = (p_unit,p_cost,SL,dis_quan,quan_of_stock_dis,brandID,supplierID)
    insert_stock_data(product)

if __name__ == "__main__":
    insert_stock_main()
    
