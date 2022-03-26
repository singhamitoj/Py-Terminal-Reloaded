import random
import time
import os
import sqlite3
import platform
import getpass
os = platform.system()
user = getpass.getuser()
print("Welcome, " + user + "!")
data = sqlite3.connect("accounts.db")
cursor = data.cursor()
c2 = data.cursor()
try:
    uip_usrname = input("Username: ")
    uip_usrpass = input("Password: ")
    cursor.execute("SELECT * FROM users where uid="+uip_usrname+" AND pass=" + uip_usrpass)
    cursor.execute()
    print(cursor.rowcount())
except:
    print("Sorry, that user does not exist.")
    exit()



try:
    lask = input("Password: ")
    c2.execute("SELECT * FROM " + lask)
    pss2 = c2.fetchall()

except:
    print("Sorry, wrong password.")
    exit()

data.commit()
data.close()

score = 0
#Change the value below to change the number of questions.
questions = 20
av = int(input("What maximum value do you want to choose for number a? "))
bv = int(input("What maximum value do you want to choose for number b? "))
st = time.time()

while questions != 0:
    a = random.randint(0, av)
    b = random.randint(0, bv)
    q = input(str(a) + "*" + str(b) + "? ")
    questions = questions - 1
    if q == str(a*b):
        print("Correct!")
        score = score + 1
    elif q != str(a*b):
        print("Incorrect!")
        score = score - 1
    et = (time.time() - st) / (20 - questions)
    print("Average time: %4.2f s" % (et))

print("\nYour score is " + str(score) + ".") 
with open("last_score.txt", "w") as s:
    s.write(user + "'s Average time: %4.2f s" % (et) + "\nYour score is " + str(score) + ".\n")
    s.close()
