#My initial attempt to get user input for a number and determine its multiplicative persistence
import math;

def persistence(num):
	import math
	return math.prod(map(int, str(num)))


def multp_pers():
	x = input("Enter a positive integer to determine its multiplicative persistence: ");
	
	#Takes user input and separates the number into a list, so I can better manipulate/ multiply it later
	
	
	counter = 0
	while len(str(x))>1:
		current_math = persistence(x)
		print(current_math+"asdf")
		counter= counter+1
	#print("The multiplicative persistence of "+str(user_input)+" is "+ str(counter))




	
multp_pers();
