# Python 3 code for hollow rectangle 

# Function to print hollow rectangle 
def frameGenerator(n) : 
	
	for i in range(1, n+1) : 
		for j in range(1, n+1) : 
			if (i == 1 or i == n or j == 1 or j == n) : 
				print("*", end="")			 
			else : 
				print(" ", end="")			 
		
		print() 

rows = 

# Driver program for above function 
rows = 8
columns = 4
frameGenerator(rows) 


# This code is contributed by Nikita Tiwari. 
