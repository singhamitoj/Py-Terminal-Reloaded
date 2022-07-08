# SQL Multiplication Tester, by singhamitoj AKA GamerSinghKing.
# Created in a garage far, far away.

# Usename: dev
# Password: alpine

import random
import time
import os
import sqlite3
import platform
import getpass
import tkinter
import webbrowser
from tkinter import END

cos = platform.system()
user = getpass.getuser()
print("Welcome, " + user + "!")

global clicker
global clickme
score = 0
clicker = 0
scorelab = 0
save = 0

def backtoshell():
    window.destroy()
    print("GOSDP has been closed. Press CTRL-C to go back to the shell.")

def weapon():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

#def savetext():
#    saved = textbox.get("1.0", END)
#    print(saved)
#    with open("text.txt", "rw") as t:
#        t.write(str(saved))
#        t.close()

def text_editor():

    editor = tkinter.Tk()
    editor.title("Text Editor")
    textbox = tkinter.Text(editor, height=15)
    def savetext():
        saved = textbox.get("1.0", tkinter.END)
        print(saved)
        with open("text.txt", "w") as t:
            t.write(str(saved))
            t.close()
    svebtn = tkinter.Button(editor, text="Save", command=savetext, bg="green")
    textbox.pack()
    svebtn.pack()
    while True:
        editor.update()


def upd():
#    updscore=1
    global score
    global scorelab
    score = score + 1
    scorelab.config(text=str(score))
    scorelab.pack()

def clicker_game():
    global score
    global scorelab
    global clicker
    score = 0
    updscore = 0
    clicker = tkinter.Tk()
    clicker.title("Simple Clicker Game")
    pattern = tkinter.PhotoImage(file="minimal-patterns.png", master=clicker)
    label = tkinter.Label(clicker, image=pattern)
    label.place(x=0, y=0)
    clickme = tkinter.Button(clicker, text="Click me!", command=upd, bg="yellow")
    scorelab = tkinter.Text(clicker, height=8)
    scorelab.insert("1.0", "Clicks: 0")
    clickme.pack()
    scorelab.pack()
    while True:
        clicker.update()
        #if updscore == 1:
        #    score = score + 1
        #    scorelab.config(text=str(score))
        #    scorelab.pack()
        #    updscore = 0

#def updscore():
#    clickme.pack_forget()
#    score = 0
#    score = score + 1
#    clickme = tkinter.Button(clicker, text=str(score), command=updscore=1, bg="yellow")
#    clickme.pack()


# The GUI function DOES NOT work as of now. Use the command only for testing and development purposes.
def gos():
    #print("This command has been disabled due to being incomplete. Remove this text and uncomment the lines below to re-enable it.")
    global window
    window = tkinter.Tk()
    window.title("GOS Development Prototype")
    window.configure(bg="cyan")
    window.geometry("1366x768")
    #wallpaper = tkinter.PhotoImage(file="Retro.png", master=window)
    #label = tkinter.Label(window, image=wallpaper)
    #label.place(x=0, y=0)
    shell = tkinter.Button(window, text = "Exit to Shell", command=backtoshell, bg="red")
    shell.place(x=5, y=-25)
    rickroll = tkinter.Button(window, text = "Self-Destruct", command=weapon, bg="red")
    #cam = tkinter.Button(window, text = "Camera Test App", command=print("Sorry, this is under development!"), bg="yellow")
    game1 = tkinter.Button(window, text="Simple Clicker Game", command=clicker_game, bg="yellow")
    textedit = tkinter.Button(window, text="Text Editor", command=text_editor, bg="blue")
    #cam.place(x=-5, y=-25)
    game1.place(x=-5, y=-25)
    game1.place(x=-5, y=-26)
    shell.pack()
    rickroll.pack()
    game1.pack()
    textedit.pack()
    #cam.pack()
    try:
        while True:
            window.update()
    except:
        print("GOSDP has been closed. Press CTRL-C to go back to the shell.")
    

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
            if cos == "Linux" or "Darwin":
                os.system("cat commands.txt")
            elif cos == "Windows":
                os.system("TYPE commands.txt")
        elif command == "gui":
            gos()

        else:
            print("Sorry, that command doesn't exist (yet).")

while True:
    log2()
