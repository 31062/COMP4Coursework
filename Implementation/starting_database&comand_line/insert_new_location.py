import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Location(LocationName) values(?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    location_name = input("locationName: ")
    location = (location_name)
    insert_data(location)
