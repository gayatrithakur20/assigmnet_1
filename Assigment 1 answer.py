#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' 1. Write a Python program to print &quot;Hello Python&quot;?
2. Write a Python program to do arithmetical operations addition and division.?
3. Write a Python program to find the area of a triangle?
4. Write a Python program to swap two variables?
5. Write a Python program to generate a random number?'''


# In[8]:



a=  print("this is a python program")


# In[9]:


' Write a Python program to do arithmetical operations addition and division.?'


# In[14]:


num1= float(input("enter the 1 number"))
num2 = float(input("enter the 2 number "))

add = num1+num2
print(add)

div = num1/num2
print(div)

    


# In[ ]:


' Write a Python program to find the area of a triangle?'


# In[15]:


def trainagle (x,y):
    a= (1/2)*x*y
    print(a)
    


# In[16]:


trainagle(3,6)


# In[17]:


'Write a Python program to swap two variables?'


# In[25]:


a= int(input("enter the 1 number before swap"))
b = int(input("eter the 2 number before swap"))


temp = a
a=b
b= temp

print("value of x after swappig is ", a)
print("value of y after swapping is ",b)


# In[28]:


# Write a Python program to generate a random number?'''
import random


# In[29]:


print(random.randint(0,100))


# In[ ]:




