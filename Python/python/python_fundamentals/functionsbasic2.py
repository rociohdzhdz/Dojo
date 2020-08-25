# Countdown accepts a number as input and returns countdown from the number to zero
def countdown(countl):
    L1=[]
    for x in range(countl,-1,-1):
        L1.append(x)
    return L1
print(countdown(9))

#Print and Return Create a function that will receive a list with two numbers. Print the first value and return the second
def PandR(L2):
    print(L2[0])
    return (L2[1])
print(PandR([12,18]))
#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def firstLength(L3):
    return L3[0]+len(L3)
print(firstLength([2,3,4,5,6]))

#Values Greater than Second

def GTS(L4):
    LNew = []
    SecV = L4[1]
    for y in range(len(L4)):
        if L4[y] > SecV:
            LNew.append(L4[y])
    print(len(LNew))
    return LNew
print(GTS([3,4,5,6,7,8]))

#This length, that value

def LengthValue(L,V):
    LNew2=[]
    for j in range(0,L,1):
        LNew2.append(V)
    return LNew2
print(LengthValue(4,6))