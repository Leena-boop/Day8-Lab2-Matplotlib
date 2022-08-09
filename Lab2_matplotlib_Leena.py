#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Leena alhabrdi 
from turtle import color
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pnd
import itertools


# In[3]:


x = np.array([1,2,3,4,5,6,7])
y = np.array([1,2,3,5,8,13,20])
plt.plot(x,y) 


# In[4]:


plt.plot(x, linestyle = '--', linewidth = 3 , marker = 'o')
plt.plot(y, linestyle = '--', linewidth = 3 , marker ='o')
plt.legend(['Normal' , 'Fast'])


# In[5]:


plt.figure(figsize=[20,5])
plt.suptitle('my data visulaization assignment',fontsize = 16)
plt.subplot(1,3,1)
x_plot1 = np.array([1, 2, 3, 4, 5, 6, 7])
y_plot1 = np.array([1, 1, 2, 3, 5, 8, 13])
plt.plot(x_plot1,y_plot1)
plt.title('First chart')

plt.subplot(1,3,2)

x_plot2 = np.array([0, 1, 2, 3, 4, 5, 6])
y_plot2 = np.array([2, 4, 6, 8, 10, 12, 14])
plt.plot(x_plot2,y_plot2)
plt.title('second chart')

plt.subplot(1,3,3)

x_plot3 = np.array([0, 1, 3, 4])
y_plot3 = np.array([4, 6, 3, 4])
plt.plot(x_plot3,y_plot3)
plt.title('third chart')


# In[7]:


My_movies = ['The fault in our stars' , 'Home alone', 'Green book']
My_movies = [7 , 9 , 8]
plt.bar(My_movies, My_movies , color = 'r' , width= 0.5)


# In[23]:


carAge = np.array([5 ,7 , 8,7, 2,17,2,9,4,11 ])
carSpeed = np.array([99,86,87,88,111,86,103,87,94,78])
plt.scatter(carAge , carSpeed ,color=['#FF0000','#00FF00','#0000FF','#00FFFF','#FF00FF','#FFFF00','#000000','#0072BD','#D95319','#7E2F8E'],alpha = 0.4, s = 350)
plt.xlabel('car age')
plt.ylabel('car speed')


# In[34]:


python_library = np.array(['numpy' ,'pandas' ,'Matplotlip' , 'Seaborn' ,'Plotly' , 'Sickit-Learn'] )
my_knowledge = np.array([9,5,10,1,2,3])
plt.pie(my_knowledge , labels = python_library , explode= [0 , 0 , 0.3 , 0 , 0 ,0] , shadow='True' ); 


# In[36]:


h = np.random.randn(250)
plt.hist(h , 15) ;


# In[ ]:




