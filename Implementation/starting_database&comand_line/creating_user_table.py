import sqlite3

#open/create new database
with sqlite3.connect("pub_stock.db") as db:
    #make the cursor
    cursor = db.cursor()
    #create sql
    sql = """create table user(
        UserID integer,
        UserFirstName text,
        UserLastName text,
        UserPhoneNumber text,
        UserEmailAddress text,
        UserCity text,
        UserStreet text,
        UserHouseNo text,
        UserPostcode text,
        primary key(UserID))"""
    #execute sql code
    cursor.execute(sql)
    #commit to database
    db.commit()
