#!/usr/bin/env python
# coding: utf-8

def mul(listu):
    product = 1
    for i in listu:
        product = product * i
    product = product % 100
    #print (product)
    if (len(str(product)) == 1):
        
        if (product == 0):
            print ('00')
        else:
            print ('0'+ str(product))  
    
    else:
        if ((str(product)) != '00'):
            print (product)
        else:
            print ('0'+ str(product))

lst = []
n = int(input("enter number of elements: "))

if (n > 0):
    for i in range(0,n):
            numbers = int(input("Enter number "+ str(i) +":"))
            lst.append(numbers)
    mul(lst)
    
else:
    print ("Invalid")


# In[ ]:




