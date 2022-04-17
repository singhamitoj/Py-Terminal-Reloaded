# SQL Multiplication Tester, by singhamitoj AKA GamerSinghKing.
# Created in a garage far, far away.
import random
import time
import os
import sqlite3
import platform
import getpass
cos = platform.system()
user = getpass.getuser()
print("Welcome, " + user + "!")

def login(username, usrpass):
    try:
        data = sqlite3.connect("accounts.db")
        crsr = data.cursor()
       #protect against SQL Injection - use parameterised queries & do not use executescript()
       # crsr.execute("SELECT * FROM users WHERE uid=? AND pass=?",(username,usrpass))
        crsr.execute("SELECT * FROM users WHERE uid=? AND pass=?",(username,usrpass))
        if crsr.fetchone():
          #  print("Allow Login")
            return (True)
        else:
           # print("Disallow Login")
            return (False)
    except:
        print("Sorry, that user does not exist.")
        return(False)
    finally:
        data.commit()
        data.close()


def tester():
    score = 0
    questions = int(input("Number of questions: "))
    av = int(input("What maximum value do you want to choose for number a? "))
    bv = int(input("What maximum value do you want to choose for number b? "))
    st = time.time()

    while questions != 0:
        a = random.randint(0, av)
        b = random.randint(0, bv)
        q = input(str(a) + "*" + str(b) + "? ")
        questions = questions - 1
        if q == str(a * b):
            print("Correct!")
            score = score + 1
        elif q != str(a * b):
            print("Incorrect!")
            if score == 0:
                pass
            else:
                score = score - 1
        et = (time.time() - st) / (20 - questions)
        print("Average time: %4.2f s" % (et))

    print("\nYour score is " + str(score) + ".")
    with open("last_score.txt", "w") as s:
        s.write(user + "'s Average time: %4.2f s" % (et) + "\nYour score is " + str(score) + ".\n")
        s.close()

def dice():
    numlist = [1, 2, 3, 4, 5, 6]
    print(str(random.choice(numlist)))

def log2():
    uip_usrname = input("Username: ")
    uip_usrpass = input("Password: ")


    if login(uip_usrname, uip_usrpass) == True:
        print("Login successful.")

    else:
        print("Login unsuccessful.")
        exit(1)


    print("Welcome to PyTerminal Reloaded!")
    time.sleep(1.5)

    while True:
        command = input(uip_usrname + "@PyTerminal:~$ ")
        if command == "tester":
            tester()
            print("Done!")
        elif command == "dice":
            dice()
        elif command == "os":
            print(cos)
        elif command == "exit":
            print("Bye")
            exit(0)
        elif command == "logout":
            break
        elif command == "help":
            os.system("cat commands.txt")

        else:
            print("Sorry, that command doesn't exist (yet).")

while True:
    log2()
