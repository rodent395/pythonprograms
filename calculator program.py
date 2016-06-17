global x
x = 1
def main():
    global x
    choice = int(raw_input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit (1-5):  "))
    if choice == 1:
        Addition()
    elif choice == 2:
        Subtraction()
    elif choice == 3:
        Multiplication()
    elif choice == 4:
        Division()
    elif choice == 5:
        raw_input('thx for using my calculator press enter to leave')
        x = 0
    else:
        print 'Invalid Choice!'

def Addition():
    x = int(raw_input('first number:'))
    y = int(raw_input('second number:'))
    print 'Your result is...   ' + str(x+y)

def Subtraction():
    x = int(raw_input('first number:'))
    y = int(raw_input('second number:'))
    print 'your result is...   ' + str(x-y)

def Multiplication():
    x = int(raw_input('first number:'))
    y = int(raw_input('first number:'))
    print 'your result is...   ' + str(x*y)

def Division():
    x = int(raw_input('first number:'))
    y = int(raw_input('second number:'))
    print 'your result is...   ' + str(x/y)
    
while x == 1:
    main()
