#!/usr/bin/env python
# coding: utf-8

# In[49]:


def order(listy, inum):
    for i in range(len(listy)-1):
        while (listy[i] > listy[i+1]):
            listy[i+1] = listy[i+1] + inum
    return listy


# In[51]:


initial_number = int(input("Enter number (greater than zero): "))
elementsNumber = int(input("Enter elements number: "))
lst = []

for i in range(0,elementsNumber):
    numbers = int(input("Enter positive number: "))
    lst.append(numbers)
        
order(lst, initial_number)


# In[ ]:




