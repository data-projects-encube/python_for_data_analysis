#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10
b=20


# In[2]:


print(a/b)


# In[3]:


print(a//b)


# In[9]:


print(500//214)


# In[14]:


fruits_basket=['orange','apple','banana']
my_fruit=input("enter your favorite fruit :")

if my_fruit in fruits_basket:
    print(f"{my_fruit} is present in the fruit basket, Awesome !!")
else:
    print(f"{my_fruit} is not in the fruit basket,sorry !")


# In[18]:


a='neeraj'

b='''neeraj
nayan
navaratna'''

print(f'my first name is {a} and full name is {b}')


# In[23]:


language="python"
print (language[4])


# In[30]:


#string operations

book_title="Data Analsysis with Python"
print(book_title.upper())
print(book_title.lower())
print(book_title.capitalize())
mybook_list=book_title.split(" ")
print(mybook_list)


# In[32]:


def is_valid_phone_num(phone_number):
    if phone_number.isdigit() and len(phone_number)==10:
        print(f"{phone_number} is valid")
        return phone_number
    else:
        print(f"{phone_number} is not valid")


# In[34]:


# Test cases
phone_numbers = [
    "1234567890",  # Valid
    "987654321",   # Too short
    "12345abcd",   # Contains non-digit characters
    "12345678901", # Too long
    "12345678901", # Too long
    "678901", # Too short
    "345678901", # Too long
    "+12345678901", # Too long
]

for phno in phone_numbers:
    is_valid_phone_num(phno)


# In[ ]:




