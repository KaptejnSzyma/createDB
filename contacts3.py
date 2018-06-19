import sqlite3

db = sqlite3.connect("contacts.sqlite")

name = input("Enter a name to search for ")

for name, phone, email in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(name)
    print(phone)
    print(email)

db.close()