
# coding: utf-8

# In[5]:


# Import the necessary libraries
import urllib
from bs4 import BeautifulSoup
import requests
import os
import lxml
from fake_useragent import UserAgent


# In[6]:


# Prevents in bot like behaviour
ua = UserAgent()
header = {'user-agent':ua.chrome}


# In[7]:


# loads the url required
url = 'http://www.barnesandnoble.com/w/mymathlab-for-trigsted-college-algebra-access-kit-kirk-trigsted/1119704911?ean=9780321923745'
page = requests.get(url,headers=header)
html = page.content
soup = BeautifulSoup(html,'html.parser')


# In[8]:


Title = soup.find('h1',{'itemprop':'name'}).text


# In[9]:


# Gets the title
Title


# In[10]:


Author = []
author=soup.find('span',{'class':'contributors'})
for i in author.find_all('a'):
    Author.append(i.text)


# In[11]:


# Gets the author name of the book
Author


# In[12]:


ISB = []
isbn=soup.find_all('div',{'class':'textbook-product-details'})
for i in isbn:
    for j in i.find_all('p'):
        ISB.append(j.text)
ISBNs=ISB[:2]


# In[13]:


# Gets the ISBN numbers
ISBNs


# In[14]:


ovw = soup.find_all('div',{'id':'productInfoOverview'})

ss=[]
for i in ovw:
    ss.append(i.find('div',{'class':'flexColumn'}))
    
Overview = []
for j in ss:
    Overview.append(j.p.text.strip())


# In[15]:


# Description
Overview


# In[16]:


prod=soup.find_all('section',{'id':'additionalProductInfo'})


# In[17]:


prodict = {}
keys = []
values = []
for i in prod:
    for k in (i.dl.find_all('dt')):
        keys.append(k.text.strip())
    for v in (i.dl.find_all('dd')):
        values.append(v.text.strip())


# In[18]:


keys


# In[19]:


values


# In[20]:


Product_Details = dict(zip(keys, values))


# In[21]:


# Gets the details of the product
Product_Details


# In[22]:


Related_Subjects = []
rel_sub = []
relsub =soup.find_all('div',{'id':'RelatedCategoriesTab'})
for i in relsub:
    for j in i.find_all('section'):
        rel_sub.append(j.ul.text.strip())
    
for i in rel_sub:
    Related_Subjects.append(i.split('\n\n'))


# In[33]:


# Gets the related Subjects
Related_Subjects


# In[24]:


toc = soup.find_all('section',{'id':'TOC'})


# In[25]:


tocl = []
for i in toc:
    tocl.append(i.find('article'))


# In[26]:


Table_c = str(tocl).split('<p>')


# In[27]:


t_o_c=Table_c[:-1]


# In[28]:


sec = []
Subsections = []

for i in t_o_c:
    if '<b>' in (i[0:4]):
        sec.append(i)
    else:
        Subsections.append(i)
        
Sections = []
sect=[]
for k in sec:
    if '<b>' in k:
        sect.append(k.replace('<b>',''))
for j in sect:
    if '</b>' in j:
        Sections.append(j.replace('</b>',''))


# In[29]:


# Sections of Table of Contents
Sections


# In[30]:


# Subections of Table of Contents
Subsections


# In[ ]:




