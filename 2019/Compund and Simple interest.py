#This script allows you to both calculate simple interest and compound interest. The user is able to choose either or.
#Created on the 13th of September 2019
Choose= input("What type of interest would you like to calculate: \n 'Compound or Simple? ")

if Choose == "compound" or "Compound":
    print("You have chosen Compounded Interest")
    p = input('Enter value of Principle ')
    n = input('Enter value of Years ')
    r = input('Enter value of Interest Rate ')

    p = int(p)
    n = int(n)
    r = float(r)

    r = (r / 100) + 1

    ci = p * ((r ** n) - 1)

    print("You will earn:", ci, 'in return')
    ci = float(ci)
    cit = p + ci
    print("You will then have a total of:", cit, 'available')
    input('Press ENTER to exit')
    exit()

if Choose == "Simple" or "simple":
    print("You have chosen Simple Interest")
    p = input('Enter value of Principle ')
    n = input('Enter value of Years ')
    r = input('Enter value of Interest Rate ')

    p = int(p)
    n = int(n)
    r = float(r)

    si = (p*r*n)/100
    print("You will earn:", si, 'in return')
    si = float(si)
    sit = p+si
    print('You will then have a total of:', sit, "available")
    input('Press ENTER to exit')

