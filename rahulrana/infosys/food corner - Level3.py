# https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693782475948032141_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    
    # to determine the type of order
    if food_type == "V":
        food_cost = 120
    elif food_type == "N":
        food_cost = 150
    else:
        return -1
    
    # to determine to bill of order
    if quantity_ordered >= 1:
        food_amount = food_cost*quantity_ordered
    else:
        return -1
        
    # determine the charge for delivery
    if distance_in_kms <= 0:
        return -1
    elif distance_in_kms <= 3:
        return food_amount
    
    delivery_charge = 0
    for i in range(4, distance_in_kms+1):
        if i <= 6:
            rate = 3
        else:
            rate = 6
            
        delivery_charge += rate
        
    bill_amount = food_amount + delivery_charge
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)