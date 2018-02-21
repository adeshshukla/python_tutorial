print()
print('--------- Nested for loops---------')
for i in range(1,6):	
	for j in range(1,i+1): 
		print(j, end=' ') # to print on the same line with space. Default it prints on next line.
		#print('\t')
	print()
print('\n') # to print two lines.

print('-------- For loop In a tuple with break ----------------')
# for i in (1,2,3,4,5,6,7,8): # this is also good
tuple = (1,2,3,4,5,6,7,8)
for i in tuple:
	if i==5:
		print(' 5 found in the list... Now breaking out...!!!!')
		break
print('\n')

print('---------- For loop In a list with continue --------------')
#list=['Adesh',28,1094.67,'IRIS','Angular',2,142]
for i in ['Adesh',28,1094.67,'IRIS','Angular',2,142]:
	if i=='IRIS':
		continue
	print(i)
print('\n')
