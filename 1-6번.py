#!/usr/bin/env python
# coding: utf-8

# In[5]:


문자열 = input('문자열 입력:')
x = False
for y in range(len(문자열)//2):
    if 문자열[y] == 문자열[-1-y]:
        x = True
        break
if x == True:
            print('회문입니다.')
else:
            print('회문이 아닙니다.')


# In[ ]:





# In[ ]:




