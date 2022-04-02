import sqlite3
import getpass
import time
user = getpass.getuser()
print("Hello, " + user + "!")
data = sqlite3.connect("accounts.db")
crsr = data.cursor()
user = input("Create Username: ")
passx = input("Create Password: ")
crsr.execute('INSERT INTO users VALUES ("' + user + '", "' + passx + '")')
data.commit()
data.close()