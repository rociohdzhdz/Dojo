#Update values in dictionary list

""" x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ] """

""" x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print (x) """
#1 change value 10 in x to 15 x = [ [5,2,3], [10,8,9] ]
def func1(L1):
    L1[1][0]=15
    return L1
print(func1([[5,2,3], [10,8,9]]))

#Change Last name of the first student from Jordan to Bryant
def funct2(L2):
    L2[0]['last_name']="Bryant"
    return L2

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print (funct2(students))

#Change Messi to Andres
def funct3(L3):
    L3['soccer'][0]="Andres"
    return L3
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(funct3(sports_directory))

#Iterate through a list of dictionaries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(L4):
    for y in L4:
        fstr = ''
        for curr_key in y.keys():
            fstr = f"{curr_key} - {y[curr_key]}, "
            print(fstr)
iterate_dictionary(students)

#Get values from a list dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary2(kname, L5):
    for j in L5:
        print(j[kname])
iterate_dictionary2('last_name',students)

#Iterate through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def funct6(L6):
    for f6 in L6.keys():
        print(f"{len(L6[f6])}")
        for elem in L6[f6]:
            print(elem)
print(funct6(dojo))