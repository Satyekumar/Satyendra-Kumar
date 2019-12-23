#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
txt="The rain in spain"
x=re.search("The.*Spain$",txt)
print(x)


# In[3]:


import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")


# In[8]:


import re

#Return a list containing every occurrence of "ai":

str = "The rain in Spain"
x = re.findall("i", str)
print(x)


# In[9]:


import re

str = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", str)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[10]:


import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())


# In[11]:


import re

str = "The rain in Spain"
x = re.search("Portugal", str)
print(x)


# In[12]:


import re

#Split the string at every white-space character:

str = "The rain in Spain"
x = re.split("\s", str)
print(x)


# In[13]:


import re

#Split the string at the first white-space character:

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)


# In[14]:


import re

#Replace all white-space characters with the digit "9":

str = "The rain in Spain"
x = re.sub("\s", "9", str)
print(x)


# In[15]:


import re

#Replace the first two occurrences of a white-space character with the digit 9:

str = "The rain in Spain"
x = re.sub("\s", "9", str, 2)
print(x)


# In[16]:


import re

#The search() function returns a Match object:

str = "The rain in Spain"
x = re.search("ai", str)
print(x)


# In[17]:


import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.span())


# In[18]:


import re

#The string property returns the search string:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.string)


# In[19]:


import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

str = "The rain in Spain"
x = re.search(r"\bS\w+", str)
print(x.group())


# In[ ]:




