import sqlite3

def insert_producttype_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into ProductType(TypeName) values(?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_producttype_main():
    name = input("producttype : ")
    type_ = (name,)
    insert_producttype_data(type_)

if __name__ == "__main__":
    insert_producttype_main()
    
