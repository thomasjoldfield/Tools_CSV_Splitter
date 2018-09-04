
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


file_loc = input("Please paste the name of csv file, including .csv extension. (use right click to paste, cntl+v won't work)")


# In[3]:


split_data = pd.read_csv(file_loc)


# In[4]:


split_data.shape


# In[9]:


number_of_splits = int(input("How many files do you want it split into?"))


# In[10]:


number_of_splits


# In[11]:


split_data_splits = np.array_split(split_data, number_of_splits)


# In[12]:


for splits in split_data_splits:
    print(splits.shape)
split_data_splits[0].head()


# In[13]:


output_name = input("Name your output file")


# In[14]:


for i in range(int(number_of_splits)):
    split_data_splits[i].to_csv(output_name + "_" + str(i) + ".csv", index=False)


# In[ ]:


print("File split completed")

