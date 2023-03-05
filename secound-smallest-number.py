n= int(input("Enter the number of element in list : "))
list1=[]
for i in range(0,n):
    element= int(input("Enter the element : "))
    list1.append(element)

print("Created list is ",list1)
	
list1.sort()

print("Second smallest number is: ",list1[1])

print("Ayush Suryavanshi\n")
