import random
import time
import os
import sqlite3
os.system("reset")
data = sqlite3.connect("accounts.db")
cursor = data.cursor()
c2 = data.cursor()
try:
    lask = input("Username: ")
    cursor.execute("SELECT * FROM " + lask)
    pss = cursor.fetchall()
    
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
    s.write("Average time: %4.2f s" % (et) + "\nYour score is " + str(score) + ".\n")
    s.close()
