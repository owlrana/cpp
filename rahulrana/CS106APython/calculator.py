# Program for calculator
# https://www.youtube.com/watch?v=oUuIMt5KmyQ&feature=emb_logo

def main():
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The Total is " + str(total) + ".")

if __name__ == '__main__':
    main()