#!/usr/bin/env python
# coding: utf-8

# In[12]:


firstname=input("Enter your first name:=")
len(firstname)
Surname=input("Enter Your surname:=")
len(Surname)
Name=firstname+" "+Surname
print("Your Full name is "+Name)
print("Your Name having character",len(Name))


# In[18]:


fsub=input("Enter your Favourite Subject")
for letter in fsub:
    print(letter,end="-")


# In[12]:


poem="ohh,Love is Blind and Un conditional,"
print(poem)
start=int(input("Enter the Start point:"))
end=int(input("Enter the end number:"))
print(poem[start:end])


# In[1]:


msg=input("Type the word in the uppercase")
tryagain=False
while tryagain==False:
if msg.isupper:
    print("Thank You")
tryagain=True
else:
    print(tryagain)   


# In[1]:


postcode=input("Enter the postcode=")
start=postcode[0:2]
print(start.upper())


# In[1]:


name=input("Enter your name please ")
count=0
name=name.lower()
for x in name:
    if  x=="a" or x=="e" or x=="o" or x=="i" or x=="u":
         count=count+1
    print("Vowel =",count)


# In[5]:


pwd=input("ENTER the password")
pwd1=input("Enter the password again")
if pwd==pwd1:
    print("Thank you")
elif pwd.lower()==pwd1.lower():
    print("Password must be in Lower Case")
else:
    print("Incorrect Password")
    


# In[36]:


word=input("Enter the Word:")
lenght=len(word)
num=1
for x in word:
    position=lenght-num
    letter=word[position]
    print(letter)
    num=num+1


# In[42]:


list=[[2,5,8],[4,5,6],[5,6,7],[9,5,7]]
row=int(input("select a row:"))
col=int(input("Select a colomn:"))
print(list[row][col])


# In[43]:


list=[[2,5,8],[4,5,6],[5,6,7],[9,5,7]]
row=int(input("select a row:"))
print(list[row])
newvalue=input("Enter the new value")
list[row].append(newvalue)
print(list[row])


# In[47]:


list=[[2,5,8],[4,5,6],[5,6,7],[9,5,7]]
row=int(input("select a row:"))
print(list[row])
col=int(input("select a col:"))
print(list[col])
change=input("Do you want to change the value (y/n):")
if change=="y":
    newvalue=int(input("Enter the new value"))
    list[row][col]=newvalue
    print(list[row])


# In[3]:


file=open("Number.txt","w")
file.write("3, ")
file.write("4, ")
file.write("5, ")
file.write("6, ")
file.write("7, ")
file.close()


# In[ ]:


# SQL LITE


# In[ ]:




