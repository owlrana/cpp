# Write the pseudocode & a program to input credits of a
# Code for Cause Campus leader and then output the badge of
# the lead on the basis of the following criteria:
# a. 7500 <= credits : Tera leader
# b. 6000 <= credits < 7500 : Gega leader 
# c. 4500 <= credits < 6000 : Mega leader 
# d. Credits < 4500 : Rising Star

def leader_status(credits):
    if credits < 4500:
        status = "Rising Star"
    elif credits < 6000 and credits >= 4500:
        status = "Mega Leader"
    elif credits < 7500 and credits >= 6000:
        status = "Gega Leader"
    else:
        status = "Tera Leader"

credits = input("Enter the credits of Code for Cause Campus Leader")
print(leader_status(credits))