# https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693780491968512136_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course
# lex_auth_012693780491968512136

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    counting = True
    #Start writing your code here
    while rupees_to_make >= 5 and no_of_five:
        rupees_to_make -= 5
        no_of_five -= 1
        five_needed += 1
    
    while rupees_to_make and no_of_one:
        rupees_to_make -= 1
        no_of_one -= 1
        one_needed += 1
        
    if rupees_to_make > 0:
        print(-1)
    else:
        print("No. of Five needed-", five_needed)
        print("No. of One needed-", one_needed)

#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
rupee = int(input("Due Money: "))
five = int(input("Number of Five coins: "))
one = int(input("Number of One coins: "))

make_amount(rupee,five,one)