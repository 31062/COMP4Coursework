import sqlite3

def insert_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into User(UserFirstName,UserLastName,UserPhoneNumber,UserEmailAddress,UserCity,UserStreet,UserHouseNo,UserPostcode) values(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    f_name = input("first name: ")
    l_name = input("last name: ")
    phone_number = input("phone number: ")
    email = input("email: ")
    city = input("city: ")
    street = input("street: ")
    house_no = input("house_no: ")
    postcode = input("postcode: ")
    name = (f_name,l_name,phone_number,email,city,street,house_no,postcode)
    insert_data(name)
