#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


# In[11]:


loan_df =pd.read_csv(r"E:\Loan Data\Bank Personal Loan Modelling.csv")
loan_df


# In[12]:


loan_df.head()


# In[13]:


loan_df.isna().sum()


# In[15]:


loan_df.shape


# In[16]:


loan_df.info()


# In[49]:


loan_df


# In[50]:


#categorical variables to be understood in details-
x=loan_df[['ID','ZIP Code','Education','Personal Loan','Securities Account','CD Account','Online','CreditCard']]
print(x.isnull().sum())

x['Education']=x['Education'].replace({1:'Undergrad',2:'Graduate',3:'Advanced/Professional'})
x['Education'].value_counts()

x['Personal Loan']=x['Personal Loan'].replace({1:'Yes',0:'No'})
x['Personal Loan'].value_counts()

x['Securities Account']=x['Securities Account'].replace({1:'Yes',0:'No'})
x['Securities Account'].value_counts()

x['CD Account']=x['CD Account'].replace({1:'Yes',0:'No'})
x['CD Account'].value_counts()

x['Online']=x['Online'].replace({1:'Yes',0:'No'})
x['Online'].value_counts()

x['CreditCard']=x['CreditCard'].replace({1:'Yes',0:'No'})
x['CreditCard'].value_counts()

x['ZIP Code']=x['ZIP Code'].astype(object)
x['ID']=x['ID'].astype(object)
x.info()


# In[51]:


x


# In[21]:


#continuous variables to be understood in details-
y=loan_df[['Age','Experience','Income','Family','CCAvg','Mortgage']]
y.info()


# In[23]:


# Statistical summary of the 2 variables
print(x.describe().T) #For categorical variables
print(y.describe().T) #For continuous variables


# In[25]:


#Measures of central tendency for contineous variables-
print('Mean for the variables--')
print(y.mean().T)
print('Median for the variables--')
print(y.median().T)
print('Mode for the variables--')
print(y.mode().T)


# In[48]:


#Measures of dispersion for contineous variables- 
print('Variance for the variables--')
print(y.var())
print('Standard Deviation for the variables--')
print(y.std())
print('Skewness for the variables--')
print(y.skew())
print('Kurtosis for the variables--')
print(y.kurt())


# In[28]:


#results:
#1. As we can see that Age, Experiance, Income, Family is having a nagative kurtosis i.e, it will have a flat peak where multiple modes will occur.
#2. CCAvh and Mortgage are having Positive Kurtosis
#3. Income, CCAvg, Mortgage are having Right Skewed data or having Right Tail
#4. Family is having a symetric distribution of data


# In[29]:


#What statistical method will you use to examine the presence of a linear relationship between age and experience variables? 
#Also, create a plot to illustrate this relationship.

# 1) To determine the presence of linear relationship between age and experience, we will use correlation.
# 2)  In addition to that, we will use the scatter plot to visualize the relationship between these two variables. 


# In[31]:


corr_1=y[['Age','Experience']].corr()
print(corr_1)


# In[33]:


sns.scatterplot(x='Age',y='Income',data=y)


# In[34]:


#Result - 
# 1. There exists a strong, non-linear, positive correlationship between Age and Income as,
# 2. The value of pearson's correlation coefficient is higher than 0.85 and 
# 3. The scatter plot is not showcasing any kind of linearity pattern for the relationship between these two variables. 


# In[37]:


# What is the most frequent family size observed in this dataset?
z=y['Family'].mode()
print(z)
z=y['Family'].value_counts()
print(z)


# In[38]:


#Result - most frequest family size recorded in the data set is 1. 


# In[40]:


# What is the percentage of variation you can observe in the ‘Income’ variable?
print(y['Income'].skew())


# In[41]:


#Result -
# As the skewness value for the income variable lies inbetween (-1 to 1), i.e. aceptable range, 
# we can use mean and standard deviation to determine the percentage of variation. 


# In[43]:


y['Percent_Variation_for_Income']=(y['Income'].std()/y['Income'].mean())*100
print(y['Percent_Variation_for_Income'].mean())
y


# In[44]:


#Result - The income variable showcases 62.4% of variation, which indicates that it has higher dispersion/spread.


# In[52]:


# The ‘Mortgage’ variable has a lot of zeroes. Impute with some business logical value that you feel fit for the data.
print(y['Mortgage'].mean()) #Before imputation
y['Mortgage'].replace({0:y['Mortgage'].mean()}) #After imputation
print(y['Mortgage'].isnull().sum())
sns.histplot(data=y, x='Mortgage')


# In[53]:


#Here all the null values are filled by using the mean, as the mortgage variable is continuous in nature 
#and median for the variable is before replacing is coming as 0.


# In[57]:


#Plot a density curve of the CCAvg variable for the customers who possess credit cards and write an interpretation about its distribution.

newloan_df=pd.concat([x,y],axis=1)
newloan_df
newloan_df.info()

f1=newloan_df.loc[new_df['CreditCard'].str.contains('Yes')]
f1.info()
sns.kdeplot(data=f1,x='CCAvg')
plt.title('CCAvg_Density_Plot')

print('Skewnes for the CCAvg is-')
print(f1['CCAvg'].skew())
print('Kurtosis for the CCAvg is-')
print(f1['CCAvg'].kurt())
print('Variance for the CCAvg is-')
print(f1['CCAvg'].var())


# In[58]:


# Result-
# The density plot indicates that the variable observes high spread and deviation from the mean.
# The plot also showcases that, the distribution of the variable is righly skewed (Asymmetric dstribution)
# Finally, as the value of kurtosis is 2.64, it can be considered as mesokurtic curve.


# In[62]:


# Do you see any outliers in the dataset? If yes, what plot you would think will be suitable to showcase to the stakeholders?
x2=y.drop(['Percent_Variation_for_Income'],axis=1)
x2
sns.boxplot(data=x2)
plt.title('Boxplot_for_Continuous_Variables_Under_Study')
      


# In[63]:


#There exists a distinct outliers in the dataser for variables namely, Income, CCAvg, and Mortgage.
# Box plot is used to visualize the presence of distinct outliers in the dataframe, 
#hence we have used the boxplot to visualize the outliers for the above mentioned continuous variables. 


# In[65]:


#Give us the decile values of the variable ‘Income’ in the dataset.
a_1=x2['Income'].sort_values()
deciles = [a_1.quantile(i/10) for i in range(1, 10)]
print('Deciles_for_Income_Variable-',deciles)


# In[67]:


# Give the IQR of all the variables which are quantitative and continuos
x2 #Dataframe containing all the continuous & quantitative variables.
A=x2.quantile(0.25)
B=x2.quantile(0.75)
IQR=(B-A)
print('IQR_for_Continuous_Variables_are_as_follows-')
print(IQR)


# In[80]:


#Do the higher-income holders spend more on credit cards?

#To filterout the higher-income holders from the dataframe, 
# we have created a class for income holders present after the 70.0% (1/7th of decile) of income 
#and called as high-income holders and accordingly created a new dataframe.

x3=newloan_df.loc[(newloan_df['Income']>newloan_df['Income'].quantile(0.7)) & (newloan_df['CreditCard'].str.contains('Yes'))]
x3.info()


# In[81]:


#x3-This dataframe contains information for those customers, 
#which has been using the credit card and coming in a newly created high-income category group.

print(newloan_df['Income'].quantile(0.7))
print(x3['Income'].min())
print(x3['Income'].max())


# In[82]:


#Mean of income for the newly created high income customer group-
print(x3['Income'].mean())
#Mean of Avg. Spending of credit cards for the newly created high income customer group-
print(x3['CCAvg'].mean())


# In[89]:


x4=newloan_df.loc[(new_df['Income']<new_df['Income'].quantile(0.7)) & (new_df['CreditCard'].str.contains('Yes'))]
x4.info()


# In[86]:


#Mean of income for the remaining customers-
print(x4['Income'].mean())

#Mean of income for the remaining customers-
print(x4['CCAvg'].mean())


# In[88]:


#How many customers use online banking? Do customers using bank internet facilities have higher incomes?

x5=newloan_df.loc[(newloan_df['Online'].str.contains('Yes'))]
x5.info()
x6=newloan_df.loc[(new_df['Online'].str.contains('No'))]
x6.info()
print(x5['Online'].value_counts())
print('Mean for the customers that are using online banking-',x5['Income'].mean())
print('Mean for the customers that are not using online banking-',x6['Income'].mean())


# In[94]:


# Result-
# 1) A total of 2984 customers are using the online banking.
# 2) Customers who have opted for online banking have higher income, as their income mean (74.31) is higher than 
#    the mean of customers who have not opted for online services (72.97)


# In[95]:


# Using the z-score of the income variable, find out the number of observations outside the +-3σ.

from scipy.stats import zscore


# In[96]:


new_df['Income'].info()
mean=new_df['Income'].mean()
SD=new_df['Income'].std()
print(mean)
print(SD)


# In[98]:


new_df['z_score'] = zscore(new_df['Income'])
outliers = new_df[abs(new_df['z_score']) > 3]
num_outliers = len(outliers)
outliers


# In[ ]:


#Result- 
# There are a total of 2 outliers present outside the +-3σ range.

