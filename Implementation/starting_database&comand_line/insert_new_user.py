import sqlite3

def insert_user_data(values):
    #open/create new database
    with sqlite3.connect("pub_stock.db") as db:
        #make the cursor
        cursor = db.cursor()
        #create sql
        sql = """insert into User(UserFirstName,UserLastName,UserPhoneNumber,UserEmailAddress,UserCity,UserStreet,UserHouseNo,UserPostcode) values(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,values)
        db.commit()

def insert_user_main():
    f_name = input("first name,str: ")
    l_name = input("last name,str: ")
    phone_number = input("phone number,str: ")
    email = input("email,str: ")
    city = input("city,str: ")
    street = input("street,str: ")
    house_no = input("house_no,str: ")
    postcode = input("postcode,str: ")
    name = (f_name,l_name,phone_number,email,city,street,house_no,postcode)
    insert_user_data(name)

if __name__ == "__main__":
    insert_user_main()
    
