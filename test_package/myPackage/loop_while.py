def loopWhile():
	print('\n--------- Print Numbers using While loop ---------')
	i = 1
	while(i<=10):
		if(i!=10):
			print(i*2, end=',')
		else:
			print(i*2)
		i+=1

def SumDigits():
	print('--------- Calculate sum of digits 153 ---------')
	n=153  
	sum=0  
	while n > 0 :
		r = n % 10
		#print(r)
		sum += r
		n = n//10 # '//' returns whole division
		#print(n)
	print(sum)