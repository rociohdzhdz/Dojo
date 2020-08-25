#1  This will return 5
def a():
    return 5
print(a())

#2 This will return 10, as the print of a() plus a()
def a():
    return 5
print(a()+a())

#3 This will returns 5 because only the first return will be printed, the second never will be printed
def a():
    return 5
    return 10
print(a())

#4 This will return 5
def a():
    return 5
    print(10)
print(a())

#5 I thought this will only returns 5 but instead returns 5 plus None
def a():
    print(5)
x = a()
print(x)

#6 this will print first 1 + 2, (3), then 2 + 3 (5) and finally 8
def a(b,c):
    print(b+c)
#print(a(1,2)+a(2,3))

#7 This will return 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

""" #8 
def a():
    b = 100
    print(b)
    if b<10:
        return 5
	else:
        return 10
    return 7
print(a()) """

#9 This will returns 7, 14 and 21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10  This will returns 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 Will return 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 Print 500, 500, 300, 500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13 I guess this will Print 500, 500, 300, but instead it printed 500,500,300, 300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14 Returns 1,3 and 2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15 Print 1, 3,5,10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)