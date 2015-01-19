import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Transactions(TransactionsTimeDate,UserID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    trans_time_date = input("TransactionsTimeDate,str :")
    user_id = int(input("UserID,int :"))
    transactions = (trans_time_date,user_id)
    insert_data(transactions)
