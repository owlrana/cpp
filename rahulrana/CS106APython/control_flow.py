# to see the control flow in python (loops, if else etc)

counter = 0
done = True
while counter <= 10 and not done:
    pass # pass is like a placeholder, if you leave a loop empty it gives error

words = ['hello', 'world', 'what', 'is', 'this']

for word in words:
    print(word)

if counter != 0:
    print("Counter is not zero")
elif counter == 1:
    print("Counter is not 1")
elif counter == 2:
    print("Counter is not 2")
else:
    print("whatever idk what counter is...")

#Ternary operator like C++ in Python
n = abs(n) if n<0 else n 

# list comprehension to make lists using loop 
# (we make lists so often that this is necessary)

sq_list = []
for x in range (1,11):
    sq_list.append(x*x)

#other readable and better method:
sq_list = [x*x for x in range(1,11)]

#suppose if you want only odd numbers:
sq_list = [x*x for x in range(1,11) if x%2 != 0]

# list of no vowels and changed to caps
caps_consonants = [ch.upper() for ch in 'Rahul Rana' if ch not in 'aeiou']