from array import *

# functions are imported
# programme is getting executed

print("type 1 to execute the array assignment programme")
print("type 2 to end the programme")
print("please note that the index value starts fro 0 'not 1' ")
print()

l = int(input("specify the function you needed"))

if l == 1:
        vals = array("i", [])

        n = int(input("the number of elements you need to put in the semi array"))

        for i in range(n):
            y = int(input(print("element", i)))
            print()
            vals.append(y)
        print()

        print(vals)

        print("we have added your desirable value")
        print("we are done")
print()

print("type 0 to search for your index value")
print("type 1 to end the programme without the search")
print("for deleting the required input 'please enter the pin' ")
print()

m = int(input("please enter the specific function that you needed to execute"))

if m == 0:
        a = int(input("please enter the value you were searching for"))
        k = 0
        for e in vals:
            if e == a:
                print(k)
                break
            k = k+1

elif m == 1:
    if l == 2:
            print("we have successfully closed the programme")
            print("bye")

    print("thank you for being with us")


elif m == 1207:

    print(" if you do know the value... just press the a number rather than 3 ")
    print()
    x = int(input(print(" if you do not know the index value of what you needed, please type 3 ")))

    if x == 3:
        a = int(input("please enter the function value you were searching for"))

        print()

        k = 0
        for e in vals:
            if e == a:
                print(k)
                break
            k = k + 1
            print("we hopefully searched for your required value")
        print()

    u = int(input("please enter the index value of the function you needed to delete"))
    print()
    if x != 3:
        vals.pop(u)

print(vals)

if l == 2:
    print(" the programme has end ")

print()

print("bye and take care")