import sqlite3
import getpass
import time
user = getpass.getuser()
print("Hello, " + user + "!")
time.sleep(1)
creornot = input("Would you like to create an account for the Tester? (y/n) ")
