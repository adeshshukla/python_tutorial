# Function : Calculate percentage 
def calculatePercentage(marksList):
	cnt = len(marksList)
	total = cnt * 100
	sum = 0
	for i in marksList :
		sum += i
	
	perc = sum/total * 100
	return perc
	
# Function : Print Details
def DisplayReportCard(rollNo, name, marksList, perc):
	print("\n\n------------------------- Report Card ----------------------")	
	print("Roll No. : ", end='\t')
	print(rollNo)
	print("Name : ", end='\t\t')
	print(name)
	print("\t Physics", end='\t') 
	print(marksList[0])
	print("\t Chemistry", end='\t') 
	print(marksList[1])
	print("\t Maths", end='\t\t')
	print(marksList[2])
	print("\n\t Percentage", end='\t') 
	print(perc)

# ---------------------------------------main function -------------------------------------------------
# declare marks List.
marks = []

# read input from console.
rollNo = int(input("Enter Roll No : "))
name = input("Enter Name : ")
phy = float(input("Enter marks in Physics : "))
chem = float(input("Enter marks in Chemistry : "))
math = float(input("Enter marks in Math : "))

# Add marks to the marks list.
marks.append(phy)
marks.append(chem)
marks.append(math)

# Calculate percentage
perc = calculatePercentage(marks)

# Call DisplayReportCard()
DisplayReportCard(rollNo, name, marks, perc)
	