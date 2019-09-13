#This is my first python code related to finance, it is a simple script that allows you to calculate the compounded interest of a Principle.
#Created on the 12th of September 2019
p= input('Enter value of Principle')
n= input('Enter value of Years')
r= input('Enter value of Interest Rate')

p= int(p)
n= int(n)
r= float(r)

r= (r/100)+1

ci= p*((r**n)-1)

print ("You will earn:",ci, 'in return')
ci= float(ci)
cit= p+ci
print ("You will then have a total of:",cit, 'available')
input ('Press ENTER to exit')
