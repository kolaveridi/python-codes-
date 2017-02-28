import os
x=os.getcwd()
print(x)#print the director
# make a new directory
os.mkdir('cool directory')
import time
time.sleep(2)

os.rename('cool directory','changed')

