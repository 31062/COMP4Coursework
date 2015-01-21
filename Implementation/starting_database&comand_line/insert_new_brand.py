import sqlite3

def insert_brand_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Brand(BrandName) values(?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_brand_main():
    name = input("brand name: ")
    brand = (name,)
    insert_brand_data(brand)

if __name__ == "__main__":
    insert_brand_main()
    
