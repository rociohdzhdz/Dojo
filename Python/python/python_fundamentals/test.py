#Temp arrays in jscript
""" var arr = [1,3,5,7];
var temp = arr[0];
arr[0] = arr[1];
arr[1] = temp; """

#Temp arrays in python
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
print(arr[1])
