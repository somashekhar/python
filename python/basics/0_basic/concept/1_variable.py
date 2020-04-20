'''
variables
variables_name = value
'''
from builtins import str

a = b = c = 1

x, y, z = 1, 2.9, "Som"

print("The value of a: " + str(a) + " b: "+ str(b) + " c: "+ str(c) +"\n")

print("The value of x: " + str(x) + " y: "+ str(y) + " z: "+ str(z) +"\n")



'''
When you want to use a global variable declare it before functions and then use a global key to access it inside the functions
'''
name = 'Som'

def update_name():
  global name
  name = "Soma"

print(name)
update_name()
print(name)
  
