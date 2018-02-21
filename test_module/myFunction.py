# SyntaxError: non-default argument follows default argument
# def printDetails(id=1001,name,age=26) :

# function definition
def printDetails(id,name,age=26) :
	print("\nId : ", id)
	print("Name : ", name)
	print("Age : ", age)

# Code for function calling
print('---------------- Position based parameter Passing -------------------')
printDetails(1831,'Adesh',26)
print('---------------- Passing any type of data ---------------------------')
printDetails('Abhi',24,1832)
print('---------------- Not Passing last optional parameter ----------------')
printDetails(1833, 'Utk')
print('---------------- Named argument Passing in any order ----------------')
printDetails(name='Saurabh', age=30, id=1834)
# TypeError: printDetails() got an unexpected keyword argument 'Id'
# printDetails(name='Saurabh', age=30, Id=1834)


print('\n\n---------------- Anonymous/ Lambda Functions ------------------------')
area=lambda a,b : a*b
print('Area of rectangle : ', area(7,5))
	