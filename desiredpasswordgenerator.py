import random
from time import sleep
import string
#the modules are imported

print(
    "Disclaimer! : If the particular block of code of this application ever runs again It is because you have given a"
    "wrong input in a wrong place,"
    "It is better to give a right input at a right place"
    )

print()
print("The password generator is now running")
print(), sleep(0.7)

def Rblock1(): #forming a nested function allows you to make exception recursively 
    try: 
        def Rblock2():
            global a
            a = []
            l = int(input("please enter the numbers of *NUMBERS* that you like to add to your password"))
            for i in range(l):
                s = int(input("please enter the number"))
                a.append(s)
            print("some selected values are -", a)
            return a
        Rblock2()
    except ValueError as e:
        sleep(0.3), print("'UHHH....' Seems like u have committed a small error, Please enter from **The first** again "
                          "'*In "
                          "a"
                          "*proper manner*'"), print()
        print(e, ValueError)                                                                                                     
        Rblock1() #In exception it goes iterates again from the first like a new code 
    finally:
        print("we are safe and done with Numbers block")
        print(a)
Rblock1()#The functions are actually called out

sleep(0.5)
print(), print("Now, the alphabets 'either Caps or small its ur wish'")

#REST OF THE CODE BLOCKS CAN BE UNDERSTOOD EASILY AND MOST ARE LIKE Rbllock1()

def Rblock3():
    def Rblock4():
        global b, t
        b = []
        m = int(input("please enter the number of *ALPHABETS* that you like to have in ur password"))
        for j in range(m):
            t = input("please enter the alphabets you desire to insert to your password")
            b.append(t)
        print("the selected values were - ", b)
        if t not in string.ascii_letters:
            sleep(0.3)
            print("it seems like you have committed some errors. So, It would be better to insert the values from "
                  "first 'The error might be raised for an incorrect input somewhere'")
            Rblock3()
            print("the alphabets that are selected are -", b)
        else:
            pass
        return b
    Rblock4()
Rblock3()

sleep(0.5)
print(), print("Now the symbols 'For additional security'")

def Rblock5():
    def Rblock6():
        global c, u
        c = []
        n = int(input("please enter the number of *SYMBOLS* that you like to have in your password"))
        for k in range(n):
            u = input("please enter the symbols you would like to have in your password")
            c.append(u)
        print("the symbols you  desired are - ", c)
        if u not in string.punctuation:
            sleep(0.3), print("It seems like you have mad e some errors 'Error might be a incorrect input', *So, "
                              "We recommend you "
                              "to mark the characters well again*")
            Rblock5()
        else:
            pass
    Rblock6()
Rblock5()

sleep(0.5), print("the request has been processed")
d = (a + b + c)

def Rblock7():
    def Rblock8():
        global tt
        try:
            tt = int(input("please enter the number of times your password needs to be shuffled"))
            for qw in range(tt):
                random.shuffle(d)
            print(), sleep(0.2)
            for q1 in d:
                print(q1, end="")
            print("We are safe and done with the full block")
        except TypeError or ValueError as e:
            print(e, "Looks like you have committed a small error in input of shuffling")
            Rblock7()
    Rblock8()
Rblock7()
sleep(0.0), print("Thank you for using my services mam/sir")
