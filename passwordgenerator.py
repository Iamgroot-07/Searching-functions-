import random

a = []
l = int(input("please enter the numbers of number that you like to add to your password"))
for i in range(l):
    s = int(input("please enter the numbers that you like to add to your password"))
    a.append(s)
print("some selected values are -", a)
print()
b = []
m = int(input("please enter the number of alphabets that you like to have in ur password"))
for j in range(m):
    t = input("please enter the alphabets you desire to insert to your password ")
    b.append(t)
print("the alphabets that are selected are -", b)
print()
c = []
n = int(input("please enter the number of symbols that you like to have in your password"))
for k in range(n):
    u = (input("please enter the symbols you would like to have in your password"))
    c.append(u)
print("the symbols you  desired are - ", c)

d = (a + b + c)
random.shuffle(d)

for q1 in d:
    print(q1, end="")
