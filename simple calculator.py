# here i will make a simple calculator and this is my first project in python

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def exit():
    print("Exiting the calculator.")
    print("Goodbye!")
    quit()

print("Select option.")
print("1, Add")
print("2, Subtract")
print("3, Multiply")
print("4, Divide")  
print("5, Exit")

choice = input("Enter choice(1/2/3/4/5):")

if choice in ('1','2','3','4','5'):
    print("You have selected option " + choice)

if choice == '5':
    exit()
    print("Enter two numbers:")


num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == '1':
    print(float(num1 + num2))
elif choice == '2':
    print(float(num1 - num2))
elif choice == '3':
    print(float(num1*num2))
elif choice== '4':
    print(float(num1/num2))
else:
    print("please enter the numbers correctly")



while True:
    print("Do you want to perform another calculation? (yes/no)")
    
    answer = input()

    if answer == "yes":
        print("Select option.")
        print("1, Add")
        print("2, Subtract")   
        print("3, Multiply")
        print("4, Divide")
        print("5, Exit")
    if answer == "5":
        exit()
    if answer == "no":
        break
    choice = input("Enter choice(1/2/3/4/5):")

    if choice in ('1','2','3','4','5'):
        print("You have selected option " + choice)
    if choice == '5':
        exit()
    else:
        print("Enter two numbers:")
    
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if choice == '1':
        print(float(num1 + num2))
    elif choice == '2':
        print(float(num1 - num2))
    elif choice == '3':
        print(float(num1*num2))
    elif choice== '4':
            print(float(num1/num2))
    elif answer == "no":
        break
    else:
        print("Please type 'yes' or 'no'.")
print("Thank you for using the calculator.")

# this is a simple calculator that can add, subtract, multiply and divide two numbers
# this is my first python project so the codes may not be very efficient and messy but it works to an extent
# i will improve it in future projects
