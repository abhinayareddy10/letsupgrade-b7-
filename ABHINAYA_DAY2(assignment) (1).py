#!/usr/bin/env python
# coding: utf-8

# # LIST and DEFAULT functions
# 

# In[1]:


#list means collection of data
a=[1,"a"]
a


# In[ ]:


#list & it's 5 default fuctions
#sort,append,extend,max,pop


# In[3]:


#sort : sorts the list in ascending order
a=[5,2,9]
a.sort()
a


# In[5]:


#append : adding certain element(only one element) at last of the list
a=[1,2,3]
a.append(4)
a


# In[6]:


#extend : adding multiple elements
a=[1,2,3]
a.extend([4,5])
a


# In[8]:


#max : finding maximum number in a list
a=[456,467,489.1,489.5]
b=max(a)
print(b)


# In[13]:


#pop : removing items at index position
a=[1,2,3,4,5]
a.pop(0)
a


# # DICTIONARY and DEFAULT FUNCTIONS

# In[15]:


#dictionary {key:value}
a={"a":1,'b':2,3:4}
a


# In[ ]:


dictio#nary & it's 5 default functions
#len,clear,update,pop,get


# In[18]:


#len : length of  the cleqardictionary
dict1={'name':'abhinaya','age':19}
dict2={'name':'kaveri','age':21}
print(len(dict1))


# In[27]:


#clear
dict1={'name':'abhinaya','age':19}
print("start len:%d"%len(dict1))
dict1.clear()
print("end len:%d"%len(dict1))


# In[29]:


#update
d1={'a':1}
d2={'a':2}
d1.update(d2)
d1['a']


# In[43]:


#pop
d={1:'a',2:'b'}
d.pop(1)
d


# In[44]:


#get
d={1:'a',2:'b'}
d.get(1)
d


# # SET and DEFAULT FUNCTIONS

# In[45]:


#set means collection which is unordered and unindexed.
a={2,2,4,1,6,"a"}
a


# In[ ]:


#set & it's 5 default functions
#add,update,discard,pop,union


# In[46]:


#add
a={1,'a',2,4,4}
a.add(3)
a


# In[48]:


#update
a={1,2,2,3,3,3,4,4,4,4}
a.update([1,2,3,4])
a


# In[49]:


#discard
a={1,2,2,3,3,3,4,4,4,4}
a.discard(1)
a


# In[54]:


#pop
p={1,2,2,3,3,3,4,4,4,4}
p.pop()
p


# In[60]:


#union
a={1,'a'}
b={2,"b"}
c=a.union(b)
c


# # TUPLE and DEFAULT FUNCTIONS

# In[61]:


#tuple means collection which is ordered and unchangeable.
a=(1,1,8,2,"a")
a


# In[ ]:


#tuple & it's 5 default functions
#count,type,len,index,slicing


# In[63]:


#count
a=(2,5,3,3,"a")
a.count(3)


# In[66]:


#type
a=("akka",)
print(type(a))
b=("akka")
print(type(b))


# In[67]:


a=(1,1,25,3,"s","s")
len(a)


# In[70]:


#index
a=(0,1,1,2)
a.index(2)


# In[79]:


#slicing
a=(1,3,4,6,6)
a[0:1]


# # STRING  and DEFAULT FUNCTIONS

# In[80]:


#string means characters with quotes
a="hi"
a


# In[ ]:


#string & it's 5 default functions
#len,upper,lower,strip,swapcase


# In[82]:


#len
a="hi hi"
len(a)


# In[83]:


#upper
a="hello"
a.upper()


# In[84]:


#lower
a="HI"
a.lower()


# In[87]:


#strip
a=",,,,,rrr,,,,hi"
s=a.strip(",")
s


# In[88]:


#swapcase
a="hello HI"
b=a.swapcase()
b

