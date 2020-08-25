# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Noelle!" with the name in a variable
name = "Rocio"
print( "Hello World ", name )	# with a comma
print( "Hello World " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = "24"
print( "Hello ", name )	# with a comma
print( "Hello " + name )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f'I love eat {fave_food2} and {fave_food2}') # with an f string
#5. print Hello world using other formats
x="Hello World"
y=24
print(x.title())
print("%s and fav num %d" %(x,y))