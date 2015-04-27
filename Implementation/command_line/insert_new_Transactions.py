import sqlite3

def insert_transactions_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Transactions(TransactionsTimeDate,UserID) values(?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_transactions_main():
    with sqlite3.connect("pub_stock.db") as db:
        cursor = db.cursor()
        cursor.execute("select UserID,UserFirstName,UserLastName from User")
        user = cursor.fetchall()
    trans_time_date = input("TransactionsTimeDate,str :")
    check = False
    while not check:
        try:
            print(user)
            user_id = int(input("UserID,int :"))
            check = True
        except ValueError:
            print("datatype error")
            check = False
    transactions = (trans_time_date,user_id)
    insert_transactions_data(transactions)

if __name__ == "__main__":
    insert_transactions_main()
    
