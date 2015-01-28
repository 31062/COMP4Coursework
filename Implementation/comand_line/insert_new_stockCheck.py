import sqlite3

def insert_stockcheck_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into StockCheck(StockCheckDate,NextStockCheckDate,QuantityFound,UserID,StockID) values(?,?,?,?,?)"""        
        cursor.execute(sql,values)
        db.commit()

def insert_stockcheck_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select UserID,UserFirstName,UserLastName from User")
        user = cursor.fetchall()
        cursor.execute("select StockID from Stock")
        stock = cursor.fetchall()
    SC_date = input("stock check date,str : ")
    NSC_date = input("next stock check date,str : ")
    check = False
    while not check:
        try:
            print("{0:<6}{1:<10}{2:>15}".format("ID", "first name", "last name"))
            for each in user:
                print("{0:<6}{1:<10}{2:>10}".format(each[0], each[1], each[2]))
            print()
            userID = int(input("UserID,int : "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    check = False
    while not check:
        try:
            quantity_found = int(input("quantity found,int : "))
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
            stockID = int(input("stockID : "))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    stock_check = (SC_date,NSC_date,userID,quantity_found,stockID)
    insert_stockcheck_data(stock_check)

if __name__ == "__main__":
    insert_stockcheck_main()
   
        
    
    
    
