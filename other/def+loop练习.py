#!/usr/bin/env python
# coding: utf-8

# In[20]:


def printName(f_name, l_name, x):
    if x == "mm":
        print(l_name + " " + f_name + " " + "is sister")
    else:
        print(l_name + " " + f_name + " " + "is borther")
printName("leo","kris","mm")
printName("leo","guagua","gg")
        
    


# In[21]:


def printName(f_name, l_name, x):
    if x:
        print(l_name + " " + f_name + " " + "is sister")
    else:
        print(l_name + " " + f_name + " " + "is borther")
printName("leo","kris", True)
printName("leo","guagua", False)
        


# In[32]:


def printName(f_name, l_name, x, y):
    for i in range(1, y):
        if x:
            print(i)
            print(l_name + " " + f_name + " " + ", i love you")
        else:
            print(l_name + " " + f_name + " " + "is borther")
printName("leo","kris", True, 11)


# In[ ]:





# In[ ]:




