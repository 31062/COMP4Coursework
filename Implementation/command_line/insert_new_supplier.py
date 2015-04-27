import sqlite3

def insert_supplier_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into Supplier(SupplierName) values(?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_supplier_main():
    name = input("supplier's name,str: ")
    supplier = (name,)
    insert_supplier_data(supplier)

if __name__ == "__main__":
    insert_supplier_main()
    
