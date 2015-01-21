import sqlite3

def insert_location_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Location(LocationName) values(?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_location_main():
    location_name = input("locationName : ")
    location = (location_name,)
    insert_location_data(location)

if __name__ == "__main__":
    insert_location_main()
    
