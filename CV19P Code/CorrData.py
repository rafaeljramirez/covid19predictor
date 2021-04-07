#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

case_df = pd.read_csv("COVID19/Cases.csv")
case_df.set_index("Dates")


# In[ ]:


def corr_coeff(df,x,y):
    #calculate the mean of 2 columns
    x_bar = df[x].mean()
    y_bar = df[y].mean()
    
    #calculate the sample deviation of the 2 columns
    x_sd = df[x].std()
    y_sd = df[y].std()
    
    #standardize, multipy and then sum all the products
    
    total_cal = ((df[x] - x_bar)/x_sd) * ((df[y]-y_bar)/y_sd).sum()
    
    corr = total_cal / (df.shape[0] - 1)
    
    return corr

# I will just use the built in corr method
    

    


# In[73]:


Alabama_df = pd.read_csv("COVID19/Alabama.csv")
Alabama_df.corr()


# In[85]:


Alaska_df = pd.read_csv("COVID19/Alaska.csv")
Alaska_df.corr()


# In[76]:


Arizona_df = pd.read_csv("COVID19/Arizona.csv")
Arizona_df.corr()


# In[77]:


Arkansas_df = pd.read_csv("COVID19/Arkansas.csv")
Arkansas_df.corr()


# In[78]:


California_df = pd.read_csv("COVID19/California.csv")
California_df.corr()


# In[79]:


Colorado_df = pd.read_csv("COVID19/Colorado.csv")
Colorado_df.corr()


# In[80]:


Connecticut_df = pd.read_csv("COVID19/Connecticut.csv")
Connecticut_df.corr()


# In[81]:


Delaware_df = pd.read_csv("COVID19/Delaware.csv")
Delaware_df.corr()


# In[82]:


Florida_df = pd.read_csv("COVID19/Florida.csv")
Florida_df.corr()


# In[83]:


Georgia_df = pd.read_csv("COVID19/Georgia.csv")
Georgia_df.corr()


# In[86]:


Hawaii_df = pd.read_csv("COVID19/Hawaii.csv")
Hawaii_df.corr()


# In[87]:


Idaho_df = pd.read_csv("COVID19/Idaho.csv")
Idaho_df.corr()


# In[88]:


Illinois_df = pd.read_csv("COVID19/Illinois.csv")
Illinois_df.corr()


# In[89]:


Indiana_df = pd.read_csv("COVID19/Indiana.csv")
Indiana_df.corr()


# In[90]:


Iowa_df = pd.read_csv("COVID19/Iowa.csv")
Iowa_df.corr()


# In[91]:


Kansas_df = pd.read_csv("COVID19/Kansas.csv")
Kansas_df.corr()


# In[92]:


Kentucky_df = pd.read_csv("COVID19/Kentucky.csv")
Kentucky_df.corr()


# In[93]:


Louisiana_df = pd.read_csv("COVID19/Louisiana.csv")
Louisiana_df.corr()


# In[94]:


Maine_df = pd.read_csv("COVID19/Maine.csv")
Maine_df.corr()


# In[95]:


Maryland_df = pd.read_csv("COVID19/Maryland.csv")
Maryland_df.corr()


# In[96]:


Massachusetts_df = pd.read_csv("COVID19/Massachusetts.csv")
Massachusetts_df.corr()


# In[97]:


Michigan_df = pd.read_csv("COVID19/Michigan.csv")
Michigan_df.corr()


# In[98]:


Minnesota_df = pd.read_csv("COVID19/Minnesota.csv")
Minnesota_df.corr()


# In[99]:


Mississippi_df = pd.read_csv("COVID19/Mississippi.csv")
Mississippi_df.corr()


# In[100]:


Missouri_df = pd.read_csv("COVID19/Missouri.csv")
Missouri_df.corr()


# In[101]:


Montana_df = pd.read_csv("COVID19/Montana.csv")
Montana_df.corr()


# In[102]:


Nebraska_df = pd.read_csv("COVID19/Nebraska.csv")
Nebraska_df.corr()


# In[103]:


Nevada_df = pd.read_csv("COVID19/Nevada.csv")
Nevada_df.corr()


# In[106]:


NewHampshire_df = pd.read_csv("COVID19/New Hampshire.csv")
NewHampshire_df.corr()


# In[108]:


NewJersey_df = pd.read_csv("COVID19/New Jersey.csv")
NewJersey_df.corr()


# In[109]:


NewMexico_df = pd.read_csv("COVID19/New Mexico.csv")
NewMexico_df.corr()


# In[110]:


NewYork_df = pd.read_csv("COVID19/New York.csv")
NewYork_df.corr()


# In[111]:


NorthCarolina_df = pd.read_csv("COVID19/North Carolina.csv")
NorthCarolina_df.corr()


# In[112]:


NorthDakota_df = pd.read_csv("COVID19/North Dakota.csv")
NorthDakota_df.corr()


# In[113]:


Ohio_df = pd.read_csv("COVID19/Ohio.csv")
Ohio_df.corr()


# In[114]:


Oklahoma_df = pd.read_csv("COVID19/Oklahoma.csv")
Oklahoma_df.corr()


# In[115]:


Oregon_df = pd.read_csv("COVID19/Oregon.csv")
Oregon_df.corr()


# In[116]:


Pennsylvania_df = pd.read_csv("COVID19/Pennsylvania.csv")
Pennsylvania_df.corr()


# In[117]:


RhodeIsland_df = pd.read_csv("COVID19/Rhode Island.csv")
RhodeIsland_df.corr()


# In[118]:


SouthCarolina_df = pd.read_csv("COVID19/South Carolina.csv")
SouthCarolina_df.corr()


# In[119]:


SouthDakota_df = pd.read_csv("COVID19/South Dakota.csv")
SouthDakota_df.corr()


# In[120]:


Tennessee_df = pd.read_csv("COVID19/Tennessee.csv")
Tennessee_df.corr()


# In[121]:


Texas_df = pd.read_csv("COVID19/Texas.csv")
Texas_df.corr()


# In[122]:


Utah_df = pd.read_csv("COVID19/Utah.csv")
Utah_df.corr()


# In[123]:


Vermont_df = pd.read_csv("COVID19/Vermont.csv")
Vermont_df.corr()


# In[124]:


Virginia_df = pd.read_csv("COVID19/Virginia.csv")
Virginia_df.corr()


# In[125]:


Washington_df = pd.read_csv("COVID19/Washington.csv")
Washington_df.corr()


# In[127]:


WestVirginia_df = pd.read_csv("COVID19/West Virginia.csv")
WestVirginia_df.corr()


# In[128]:


Wisconsin_df = pd.read_csv("COVID19/Wisconsin.csv")
Wisconsin_df.corr()


# In[129]:


Wyoming_df = pd.read_csv("COVID19/Wyoming.csv")
Wyoming_df.corr()


# In[130]:


PuertoRico_df = pd.read_csv("COVID19/Puerto Rico.csv")
PuertoRico_df.corr()


# In[131]:


UnitedStates_df = pd.read_csv("COVID19/United States.csv")
UnitedStates_df.corr()


# In[ ]:




