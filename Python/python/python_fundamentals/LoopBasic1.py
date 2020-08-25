#Basic - Print integers from 0 to 150
for x in range (151):
    print(x)

#Multiples of five from 5 to 1000
for y in range(5,1000,5):
    print(y)

#Counting the Dojo Way Print Integers 1 to 100 if divisible by 5 print Coding instead if divisible by 10 print coding dojo
for CD in range(1,101,1):
    if CD % 10 ==0:
        print("Coding Dojo")
    elif CD % 5==0:
        print("Coding")
    else:
        print(CD)

#Whoa. Add odd integers from 0 to 500000 and print the final sum
sum = 0
for oddn in range (1,500000, 2):
    print(oddn)
    sum = sum+oddn
print (sum)

#Countdown by fours. Print positive numbers starting at 2018 counting down fours
for cdown in range (2018,0,-4):
    print(cdown)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum=1
highNum=14
mult=3
for flexc in range (lowNum, highNum, 1):
    if flexc % mult ==0:
        print(flexc)