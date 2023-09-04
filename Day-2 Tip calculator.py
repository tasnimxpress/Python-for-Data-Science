#!/usr/bin/env python
# coding: utf-8

# # Tip calculator
# * take input from user : 
#     * total Bill, 
#     * total people, 
#     * tip percentage
# * print how much each person should pay.
# 

# In[1]:


print('Welcome to the tip calculator.')


# In[2]:


bill_1 = input('What is the total bill? ')
bill_2 = bill_1.strip('$')
total_bill = float(bill_2)


# In[3]:


number_of_people = int(input('How many people to split the bill? '))


# In[4]:


tip_1 = input('what percentage tip would you like to give? ')
tip_2 = tip_1.strip('%')
tip_percentage = float(tip_2)


# In[9]:


tip = (tip_percentage * total_bill)/100

print(tip)
# In[10]:


payable = total_bill + tip

print(payable)
# In[11]:


each_person = round((payable/number_of_people), 1)

print(each_person)
# In[12]:


print(f'Each person should pay: ${each_person}')


# ### Day 2 Complete.
