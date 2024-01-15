while 1:
    print("CALCULATER MENU\nENTER YOUR CHOICE\n1- Addition\n2- Subtraction\n3- Multipliction\n4- Division")
    c=int(input("Enter your choice :"))
    if c>0 & c<5:
        print("enter two operand to perform operation:")
        a=int(input("Enter your first operand :"))
        b=int(input("Enter your second operand :"))
        if c==1:
            R=a+b
        elif c==2:
            R=a-b
        elif c==3:
            R=a*b
        else:
            R=a/b
        print("your result is :",R)
    else:
        print("Enter valid choice...")
    x=(input("Do you want to continue(y/n) :"))
    if x!='y':
        break
print('Calculater terminated..')