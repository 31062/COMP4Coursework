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
    stockID_list = []
    quantity_list = []
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
    again = True
    while again:
        check = False
        while not check:
            try:
                print()
                print("{0:<6}".format("ID"))
                for each_1 in stock:
                    print("{0:<6}".format(each_1[0]))
                print()
                stockID = int(input("stockID : "))
                stockID_list.append(stockID)
                check = True
            except ValueError:
                print("datatype error")
                check = False
        check = False
        while not check:
            try:
                quantity_found = int(input("quantity found,int : "))
                quantity_list.append(quantity_found)
                check = True
            except ValueError:
                print("datatype error")
                check = False
        temp = input("do u whish to add anougher stock item to this stock check;yes or no:")
        if temp not in ["y","Y","yes","Yes","YES"]:
            again = False
    count = 0
    for each in stockID_list:
        stock_check = (SC_date,NSC_date,userID,quantity_list[count],stockID_list[count])
        insert_stockcheck_data(stock_check)
        count += 1

if __name__ == "__main__":
    insert_stockcheck_main()
   
        
    
    
    
