#!/usr/bin/env python
# coding: utf-8

# In[ ]:


str = input('문자열을 입력:')
rev = ""
for x in str:
    rev = x + rev
    
print(rev)

