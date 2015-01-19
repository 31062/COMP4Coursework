import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into StockCheck(StockCheckDate,NextStockCheckDate,QuantityFound,UserID,StockID) values(?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    SC_date = input("stock check date,str : ")
    NSC_date = input("next stock check date,str : ") 
    userID = int(input("UserID,int : "))
    quantity_found = int(input("quantity found,int : "))
    stockID = int(input("stockID : "))
        
    
    
    stock_check = (SC_date,NSC_date,userID,quantity_found,stockID)
    insert_data(stock_check)
