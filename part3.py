#!/usr/bin/env python
# coding: utf-8

# In[6]:


# function to check if three sides
# form a triangle or not
def checkValidity(a, b, c):
     
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       
 
# driver code
a = 7
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid Rectangle")
else:
    print("Invalid Rectangle")


# In[ ]:




