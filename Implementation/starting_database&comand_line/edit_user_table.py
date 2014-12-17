import sqlite3

def amend_first_name(firstdata):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """update User set
            UserFirstName = ?"""
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    
