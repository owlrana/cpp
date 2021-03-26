# https://infytq.onwingspan.com/en/viewer/hands-on/lex_auth_012693788748742656146_shared?collectionId=lex_auth_0125409616243425281061_shared&collectionType=Course

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    
    if int(str(account_number)[0]) != 1 and len(str(account_number)) != 4:
        print("Invalid account number")
    
    print("Account number:", account_number)
    
    
    if account_balance < 100000:
        print("Insufficient account balance")
        
    loan_type_list = ["Car", "House", "Business"]
        
    if salary < 0 or loan_amount_expected < 0 or loan_type not in loan_type_list:
        print("Invalid loan type or salary")
    elif salary <= 25000:
        print("The customer is not eligible for the loan")
    elif salary > 25000:
        if loan_type == "Car":
            if loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 500000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    elif salary > 50000:
        if loan_type == "House":
            if loan_amount_expected <= 6000000 and customer_emi_expected <= 60:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 6000000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        elif loan_type == "Car":
            if loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 500000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    elif salary > 75000:
        if loan_type == "Business":
            if loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 500000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        elif loan_type == "House":
            if loan_amount_expected <= 6000000 and customer_emi_expected <= 60:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 6000000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        elif loan_type == "Car":
            if loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested EMI's:",customer_emi_expected)
                print("The customer can avail the amount of Rs.", 500000)
                print("Requested loan amount:", loan_amount_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Invalid loan type or salary")
    
    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    
    

    #Use the below given print statements to display the output, in case of invalid data.
    
    
    
    
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)