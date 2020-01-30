#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Cheers,Mate!")
#print("Hello,World")


# In[6]:


x=str("Hello World")
print(type(x))


# In[7]:


z=1j
print(type(z))


# In[11]:


import random
print(random.randrange(1,10))


# In[12]:


x=int(1)
y=int(2.8)
z=int("3")
print(x,y,z)


# In[13]:


x=float(1)
y=float(2.8)
z=float("3")
w=float("4.2")
print(x,y,z,w)


# In[16]:


print(10>9)
print(10==9)
print(10<9)


# In[45]:


a = 200
b = 33

if b > a:
    print("b is greater")
else:
        print("a is greater")


# In[47]:


bool("abc")
bool(12)
bool(["apple,orange,Bananas"])


# In[48]:


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# In[49]:


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# In[50]:


x=200
print(isinstance (x,int))


# In[ ]:




