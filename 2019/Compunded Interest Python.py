p= input('Enter value of Principle')
n= input('Enter value of Years')
r= input('Enter value of Interest Rate')

p= int(p)
n= int(n)
r= int(r)

r= (r/100)+1

ci= p*((r**n)-1)

print ("You will get:",ci, 'in return')
ci= int(ci)
cit= p+ci
print ("You will then have a total of:",cit, 'available')
input ('Press ENTER to exit')
