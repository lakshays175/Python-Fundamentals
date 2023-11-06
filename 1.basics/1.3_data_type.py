x = 4
#print(type(x)) 
#print(id(x))

#List 
x= ['ram','krishna']

# Dictonary
z = {'x': 10,
     'y': 20 }

#print(type(z))
#print(z['x'][0])

# List of dictionaries 
z1 = [ {1: 20}, 
       {4: 10 }]

# Type cast 
x2 = str(x)
#print(x2[0:4])

# function
def my_list(): 
    x = ['ram','krishna']
    print(x[0])

def my_sum(a,b): 
    print(a+b)

def cast_example(a):
    print(int(a))

my_list()

my_sum(3,4)

cast_example('10')