#!/usr/bin/env python
# coding: utf-8

# Creating a List.
# List starts with 0 index

# Creating a List using a constructor.

# In[1]:


newList =list(("london","paris","Switzerland","Mexico","delhi"))
print(newList)


# List with different datatypes.

# In[2]:


list_1 = ["a","b","c","d"]
list_2 = [1,-2,0.3,4,-5.11]
list_3 = [True,False]
list_4 = ["Pineapple",11,True,-0.11]
print(list_1)
print(list_2)
print(list_3)
print(list_4)


# Using append() method to add an element.
# 

# In[3]:


monthList_1 =[]

monthList_1.append("Jan")
monthList_1.append("Feb")
monthList_1.append("Mar")
monthList_1.append("Apr")

print(monthList_1)


# Using insert() method to insert an element at a specific index.

# In[4]:


monthList_2 =[]

monthList_2.insert(0,"May")
monthList_2.insert(1,"Jun")
monthList_2.insert(2,"Jul")
monthList_2.insert(3,"Aug")
monthList_2.insert(4,"Sept")
monthList_2.insert(5,"Oct")
monthList_2.insert(6,"Nov")
monthList_2.insert(7,"Dec")

print(monthList_2)



# Using extend() method to extend the list.

# In[5]:


# The elements will be added to the end of the list.

monthList_1.extend(monthList_2)

print(monthList_1)


# Removing elements from a list.

# Using remove() method.

# In[6]:


monthList_1.remove("Aug")
print(monthList_1)


# Using pop()method.

# In[7]:


monthList_1.pop()


# Using pop()  with an index to remove an element from a specific index.

# In[8]:


monthList_1.pop(0)


# Using del keyword.

# In[9]:


del monthList_1[1]
print(monthList_1)


# Using clear() method to clear the list.

# In[10]:


monthList_1.clear()

print(monthList_1)


# In[11]:


myCars = ["Lambo","BMW","Audi"]

print(myCars)


# To delete the list using del keyword.

# In[12]:


del myCars
print(myCars) 

# This will give an error because myCars list has been deleted.


# Accessing Elements in a list.

# In[14]:


languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
print(languages)


# In[15]:


# Accessing all items.
print(languages[:])


# In[16]:


# Accessing with specific index and rest all the items.
print(languages[2:])


# In[17]:


# Accessing with specific index.
print(languages[4])


# In[18]:


# Accessing last item.
print(languages[-1])


# In[19]:


# Accessing reverse items
print(languages[-3:-1])


# Using for loop to return items in a list

# In[20]:


for i in languages:
    print(i)


# In[21]:


#using range function

for i in range(len(languages)):
    print(languages[i])


# In[22]:


#using while loop

i=0
while i<len(languages):
    print(languages[i])
    i+=1


# Using comprehension

# In[23]:


[print(i) for i in languages ]


# To check for a specific item in a list

# In[24]:


if "Python" in languages:
    print("Yes")
else:
    print("No")


# Sorting a List.

# In[25]:


languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
print(languages)


# In[26]:


languages.sort()
print(languages)


# In[27]:


#Reverse Sorting

languages.sort(reverse=True)
print(languages)


# Copy a List.

# In[29]:


#Using copy()

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
newList = languages.copy()
print(newList)


# Joining Lists using different methods.

# In[30]:


City_1 = list(("London","Paris","Rome"))
City_2 = list(("Anand","Nadiad","Delhi"))

City_all = City_1 + City_2
print(City_all)


# In[32]:


City_1 = list(("London","Paris","Rome"))
City_2 = list(("Anand","Nadiad","Delhi"))

for i in City_2:
    City_1.append(i)
print(City_1)


# ## List Methods Must Know:

# list()
# append()
# insert()
# remove()
# clear()
# pop()
# sort()
# copy()
# extend()
# reverse()
# 
