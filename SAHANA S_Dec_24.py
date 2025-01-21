#!/usr/bin/env python
# coding: utf-8

# # Project Statistical Methods for Decision Making: FoodHub Data Analysis
# 
# **Marks: 60 points**

# ### Context
# 
# The number of restaurants in New York is increasing day by day. Lots of students and busy professionals rely on those restaurants due to their hectic lifestyles. Online food delivery service is a great option for them. It provides them with good food from their favorite restaurants. A food aggregator company FoodHub offers access to multiple restaurants through a single smartphone app.
# 
# The app allows the restaurants to receive a direct online order from a customer. The app assigns a delivery person from the company to pick up the order after it is confirmed by the restaurant. The delivery person then uses the map to reach the restaurant and waits for the food package. Once the food package is handed over to the delivery person, he/she confirms the pick-up in the app and travels to the customer's location to deliver the food. The delivery person confirms the drop-off in the app after delivering the food package to the customer. The customer can rate the order in the app. The food aggregator earns money by collecting a fixed margin of the delivery order from the restaurants.
# 
# ### Objective
# 
# The food aggregator company has stored the data of the different orders made by the registered customers in their online portal. They want to analyze the data to get a fair idea about the demand of different restaurants which will help them in enhancing their customer experience. Suppose you are a Data Scientist at Foodhub and the Data Science team has shared some of the key questions that need to be answered. Perform the data analysis to find answers to these questions that will help the company to improve the business.
# 
# ### Data Description
# 
# The data contains the different data related to a food order. The detailed data dictionary is given below.
# 
# ### Data Dictionary
# 
# * order_id: Unique ID of the order
# * customer_id: ID of the customer who ordered the food
# * restaurant_name: Name of the restaurant
# * cuisine_type: Cuisine ordered by the customer
# * cost_of_the_order: Cost of the order
# * day_of_the_week: Indicates whether the order is placed on a weekday or weekend (The weekday is from Monday to Friday and the weekend is Saturday and Sunday)
# * rating: Rating given by the customer out of 5
# * food_preparation_time: Time (in minutes) taken by the restaurant to prepare the food. This is calculated by taking the difference between the timestamps of the restaurant's order confirmation and the delivery person's pick-up confirmation.
# * delivery_time: Time (in minutes) taken by the delivery person to deliver the food package. This is calculated by taking the difference between the timestamps of the delivery person's pick-up confirmation and drop-off information

# ### **Please read the instructions carefully before starting the project.** 
# This is a commented Jupyter IPython Notebook file in which all the instructions and tasks to be performed are mentioned. Read along carefully to complete the project.
# * Blanks '_______' are provided in the notebook that 
# needs to be filled with an appropriate code to get the correct result. Please replace the blank with the right code snippet. With every '_______' blank, there is a comment that briefly describes what needs to be filled in the blank space. 
# * Identify the task to be performed correctly, and only then proceed to write the required code.
# * Fill the code wherever asked by the commented lines like "# write your code here" or "# complete the code". Running incomplete code may throw an error.
# * Please run the codes in a sequential manner from the beginning to avoid any unnecessary errors.
# * You can the results/observations derived from the analysis here and use them to create your final presentation.
# 

# ### Let us start by importing the required libraries

# In[2]:


# Import libraries for data manipulation
import numpy as np
import pandas as pd

# Import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns


# ### Understanding the structure of the data

# In[3]:


# uncomment and run the following lines for Google Colab
# from google.colab import drive
# drive.mount('/content/drive')


# In[5]:


# Read the data
df = pd.read_csv('foodhub_order.csv') ## Fill the blank to read the data
# Returns the first 5 rows
df.head() 


# ### **Question 1:** How many rows and columns are present in the data? [0.5 mark]

# In[6]:


# Check the shape of the dataset
df.shape ## Fill in the blank


# ### **Question 2:** What are the datatypes of the different columns in the dataset? [0.5 mark]

# In[7]:


df.info()


# ### **Question 3:** Are there any missing values in the data? If yes, treat them using an appropriate method.  [1 Mark]

# In[8]:


# Checking for missing values in the data
df.isnull().sum()  #Write the appropriate function to print the sum of null values for each column


# ### **Question 4:** Check the statistical summary of the data. What is the minimum, average, and maximum time it takes for food to be prepared once an order is placed? [2 marks]

# In[9]:


# Get the summary statistics of the numerical data
df.describe()['food_preparation_time'][['min', 'mean', 'max']] ## Write the appropriate function to print the statitical summary of the data (Hint - you have seen this in the case studies before)


# ### **Question 5:** How many orders are not rated? [1 mark]

# In[10]:


df['rating'].value_counts() ## Complete the code 


# ### Exploratory Data Analysis (EDA)

# ### Univariate Analysis

# ### **Question 6:** Explore all the variables and provide observations on their distributions. (Generally, histograms, boxplots, countplots, etc. are used for univariate exploration.) [8 marks]

# #### Order ID

# In[11]:


# check unique order ID
df['order_id'].nunique()  


# Customer ID

# In[12]:


# check unique customer ID
df['customer_id'].nunique()  ## Complete the code to find out number of unique Customer ID


# Restaurant name

# In[13]:


# check unique Restaurant Name
df['restaurant_name'].nunique()  ## Complete the code to find out number of unique Restaurant Name


# #### Cuisine type

# In[14]:


# Check unique cuisine type
df['cuisine_type'].nunique() ## Complete the code to find out  number of  unique cuisine type


# In[15]:


plt.figure(figsize = (15,5))
sns.countplot(data = df, x = 'cuisine_type') ## Create a countplot for cuisine type.


# #### Cost of the order

# In[16]:


sns.histplot(data=df,x='cost_of_the_order') ## Histogram for the cost of order
plt.show()
sns.boxplot(data=df,x='cost_of_the_order') ## Boxplot for the cost of order
plt.show() 


# #### Day of the week

# In[17]:


# # Check the unique values
df['day_of_the_week'].unique() ## Complete the code to check unique values for the 'day_of_the_week' column


# In[18]:


sns.countplot(data = df, x = 'day_of_the_week') ## Complete the code to plot a bar graph for 'day_of_the_week' column
plt.title('Number of Orders for Each Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Orders')
plt.show()


# #### Rating

# In[19]:


# Check the unique values
df['rating'].unique() ## Complete the code to check unique values for the 'rating' column


# In[20]:


sns.countplot(data = df, x = 'rating') ## Complete the code to plot bar graph for 'rating' column
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()


# #### Food Preparation time

# In[21]:


sns.histplot(data=df,x='cost_of_the_order') ## Complete the code to plot the histogram for the cost of order
plt.title('Histogram of Cost of Orders')
plt.xlabel('Cost of Order')
plt.ylabel('Frequency')
plt.show()


sns.boxplot(data=df,x='cost_of_the_order') ## Complete the code to plot the boxplot for the cost of order
plt.title('Boxplot of Cost of Orders')
plt.xlabel('Cost of Order')
plt.show()


# #### Delivery time

# In[22]:


sns.histplot(data=df,x='delivery_time') ## Complete the code to plot the histogram for the delivery time
plt.title('Histogram of Delivery Time')
plt.xlabel('Delivery Time (minutes)')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(data=df,x='delivery_time') ## Complete the code to plot the boxplot for the delivery time
plt.title('Boxplot of Delivery Time')
plt.xlabel('Delivery Time (minutes)')
plt.show()


# ### **Question 7:** Which are the top 5 restaurants in terms of the number of orders received? [1 mark]

# In[23]:


# Get top 5 restaurants with highest number of orders
df['restaurant_name'].value_counts().head(5)   ## Complete the code


# ### **Question 8:** Which is the most popular cuisine on weekends? [1 mark]

# In[24]:


# Get most popular cuisine on weekends
df_weekend = df[df['day_of_the_week'] == 'Weekend']
df_weekend['cuisine_type'].value_counts().idxmax() ## Complete the code to check unique values for the cuisine type on weekend


# ### **Question 9:** What percentage of the orders cost more than 20 dollars? [2 marks]
# 

# In[25]:


# Get orders that cost above 20 dollars
df_greater_than_20 = df[df['cost_of_the_order']>20] ## Write the appropriate column name to get the orders having cost above $20

# Calculate the number of total orders where the cost is above 20 dollars
print('The number of total orders that cost above 20 dollars is:', df_greater_than_20.shape[0])

# Calculate percentage of such orders in the dataset
percentage = (df_greater_than_20.shape[0] / df.shape[0]) * 100

print("Percentage of orders above 20 dollars:", round(percentage, 2), '%')


# ### **Question 10:** What is the mean order delivery time? [1 mark]

# In[26]:


# Get the mean delivery time
mean_del_time = df['delivery_time'].mean()  ## Write the appropriate function to obtain the mean delivery time

print('The mean delivery time for this dataset is', round(mean_del_time, 2), 'minutes')


# ### **Question 11:** The company has decided to give 20% discount vouchers to the top 3 most frequent customers. Find the IDs of these customers and the number of orders they placed. [1 mark]

# In[27]:


# Get the counts of  each customer_id
df['customer_id'].value_counts().head(3)  ## Write the appropriate column name to get the top 5 cmost frequent customers


# ### Multivariate Analysis

# ### **Question 12:** Perform a multivariate analysis to explore relationships between the important variables in the dataset. (It is a good idea to explore relations between numerical variables as well as relations between numerical and categorical variables) [9 marks]

# #### Cuisine vs Cost of the order

# In[28]:


# Relationship between cost of the order and cuisine type
plt.figure(figsize=(15,7))
sns.boxplot(x = "cuisine_type", y = "cost_of_the_order", data = df, palette = 'PuBu')
plt.xticks(rotation = 60)
plt.show()


# #### Cuisine vs Food Preparation time

# In[29]:


# Relationship between food preparation time and cuisine type
plt.figure(figsize=(15,7))
sns.boxplot(x='cuisine_type', y='food_preparation_time', data=df) ## Complete the code to visualize the relationship between food preparation time and cuisine type using boxplot
plt.xticks(rotation=60)
plt.title('Relationship between Food Preparation Time and Cuisine Type')
plt.xlabel('Cuisine Type')
plt.ylabel('Food Preparation Time (minutes)')
plt.show()


# #### Day of the Week vs Delivery time

# In[31]:


# Relationship between day of the week and delivery time
plt.figure(figsize=(15,7))
sns.boxplot(x='day_of_the_week', y='delivery_time', data=df)  ## Complete the code to visualize the relationship between day of the week and delivery time using boxplot
plt.title('Relationship between Day of the Week and Delivery Time')
plt.xlabel('Day of the Week')
plt.ylabel('Delivery Time (minutes)')
plt.show()


# #### Run the below code and write your observations on the revenue generated by the restaurants.

# In[32]:


df.groupby(['restaurant_name'])['cost_of_the_order'].sum().sort_values(ascending = False).head(14)


# #### Rating vs Delivery time

# In[37]:


# Relationship between rating and delivery time
plt.figure(figsize=(15, 7))
sns.pointplot(x = 'rating', y = 'delivery_time', data = df)
plt.title('Relationship between rating and delivery time')
plt.xlabel('Rating')
plt.ylabel('Delivery time (minutes)')
plt.show()


# #### Rating vs Food preparation time

# In[34]:


# Relationship between rating and food preparation time
plt.figure(figsize=(15, 7))
sns.pointplot(x='rating', y='food_preparation_time', data=df)  ## Complete the code to visualize the relationship between rating and food preparation time using pointplot
plt.title('Relationship between Rating and Food Preparation Time')
plt.xlabel('Rating')
plt.ylabel('Food Preparation Time (minutes)')
plt.show()


# #### Rating vs Cost of the order

# In[35]:


# Relationship between rating and cost of the order
plt.figure(figsize=(15, 7))
sns.pointplot(x='rating', y='cost_of_the_order', data=df)   ## Complete the code to visualize the relationship between rating and cost of the order using pointplot
plt.title('Relationship between Rating and Cost of the Order')
plt.xlabel('Rating')
plt.ylabel('Cost of the Order')
plt.show()


# #### Correlation among variables

# In[43]:


# Plot the heatmap 
col_list = ['cost_of_the_order', 'food_preparation_time', 'delivery_time']
plt.figure(figsize=(15, 7))
sns.heatmap(df[col_list].corr(), annot=True, vmin=-1, vmax=1, fmt=".2f", cmap="Spectral")
plt.show()


# ### **Question 13:** The company wants to provide a promotional offer in the advertisement of the restaurants. The condition to get the offer is that the restaurants must have a rating count of more than 50 and the average rating should be greater than 4. Find the restaurants fulfilling the criteria to get the promotional offer. [3 marks]

# In[44]:


# Filter the rated restaurants
df_rated = df[df['rating'] != 'Not given'].copy()

# Convert rating column from object to integer
df_rated['rating'] = df_rated['rating'].astype('int')  

# Create a dataframe that contains the restaurant names with their rating counts
df_rating_count = df_rated.groupby(['restaurant_name'])['rating'].count().sort_values(ascending = False).reset_index()
df_rating_count.head() 


# In[51]:


# Get the restaurant names that have rating count more than 50
rest_names = df_rating_count[df_rating_count['rating'] > 50]['restaurant_name'] ## Complete the code to get the restaurant names having rating count more than 50

# Filter to get the data of restaurants that have rating count more than 50
df_mean_4 = df_rated[df_rated['restaurant_name'].isin(rest_names)].copy()

# Group the restaurant names with their ratings and find the mean rating of each restaurant
df_mean_4.groupby(['restaurant_name'])['rating'].mean().sort_values(ascending = False).reset_index().dropna() ## Complete the code to find the mean rating


# ### **Question 14:** The company charges the restaurant 25% on the orders having cost greater than 20 dollars and 15% on the orders having cost greater than 5 dollars. Find the net revenue generated by the company across all orders. [3 marks]

# In[52]:


#function to determine the revenue
def compute_rev(x):
    if x > 20:
        return x*0.25
    elif x > 5:
        return x*0.15
    else:
        return x*0

df['Revenue'] = df['cost_of_the_order'].apply(compute_rev) ## Write the apprpriate column name to compute the revenue
df.head()


# In[53]:


# get the total revenue and print it
total_rev = df['Revenue'].sum() ## Write the appropriate function to get the total revenue
print('The net revenue is around', round(total_rev, 2), 'dollars')


# ### **Question 15:** The company wants to analyze the total time required to deliver the food. What percentage of orders take more than 60 minutes to get delivered from the time the order is placed? (The food has to be prepared and then delivered.)[2 marks]
# 

# In[55]:


# Calculate total delivery time and add a new column to the dataframe df to store the total delivery time
df['total_time'] = df['food_preparation_time'] + df['delivery_time']


## Write the code below to find the percentage of orders that have more than 60 minutes of total delivery time (see Question 9 for reference)
# Find the percentage of orders with more than 60 minutes of total delivery time
percentage_more_than_60 = (df[df['total_time'] > 60].shape[0] / df.shape[0]) * 100

# Print the percentage
print("Percentage of orders with more than 60 minutes of total delivery time:", round(percentage_more_than_60, 2), '%')


# ### **Question 16:** The company wants to analyze the delivery time of the orders on weekdays and weekends. How does the mean delivery time vary during weekdays and weekends? [2 marks]

# In[58]:


# Get the mean delivery time on weekdays and print it
print('The mean delivery time on weekdays is around',round(df[df['day_of_the_week'] == 'Weekday']['delivery_time'].mean()),'minutes')


## Write the code below to get the mean delivery time on weekends and print it


# Get the mean delivery time on weekends and print it
weekend_mean_delivery_time = df[df['day_of_the_week'] == 'Weekend']['delivery_time'].mean()
print('The mean delivery time on weekends is around', round(weekend_mean_delivery_time), 'minutes')


# ### Conclusion and Recommendations

# ### **Question 17:** What are your conclusions from the analysis? What recommendations would you like to share to help improve the business? (You can use cuisine type and feedback ratings to drive your business recommendations.) [6 marks]

# # Conclusions:
# 
# * Top Restaurants: Identified the top 5 restaurants based on the number of orders received. These restaurants play a significant role in the business.
# * Cuisine Analysis: Explored the relationship between food preparation time and cuisine type. This analysis could help in optimizing kitchen processes and improving overall efficiency.
# * Rating Distribution: Analyzed the distribution of ratings to understand customer satisfaction. Most orders received average to high ratings, indicating overall customer contentment.
# * Cost Analysis: Explored the distribution of the cost of orders. This could provide insights into pricing strategies and customer preferences.
# * Delivery Time: Investigated mean delivery times and found variations during weekdays and weekends. This information is crucial for managing customer expectations and delivery logistics.
# * Revenue Generation: Calculated revenue based on the company's charging policies. This information is vital for financial planning and profit analysis.
# * Total Delivery Time: Explored the percentage of orders taking more than 60 minutes for total delivery time. This could highlight areas for improvement in the delivery process.
# 

# # Recommendations:
# 
# * Focus on Top Restaurants: Strengthen partnerships with the top 5 restaurants to enhance business volume and customer satisfaction.
# * Optimize Food Preparation: Collaborate with restaurants to optimize food preparation times, particularly for cuisines with longer preparation times. This could improve overall delivery efficiency.
# * Customer Satisfaction Programs: Implement programs to improve customer satisfaction, especially for restaurants with lower ratings. Gather customer feedback to identify specific areas for improvement.
# * Pricing Strategy: Evaluate the cost distribution and consider adjusting pricing strategies. Provide promotions or discounts for orders with potential for higher revenue.
# * Delivery Logistics: Fine-tune delivery logistics based on variations in mean delivery times during weekdays and weekends. Ensure efficient routes and timely deliveries.
# * Promote Popular Cuisines: Leverage the popularity of certain cuisines by promoting them through marketing campaigns. Consider offering deals or promotions for these cuisines to attract more orders.
# * Efficient Revenue Models: Continuously monitor and optimize revenue models. Explore opportunities for partnerships and collaborations to increase overall revenue.
# * Improve Total Delivery Time: Identify and address factors contributing to orders taking more than 60 minutes for total delivery time. Optimize processes to enhance customer experience.
# * By implementing these recommendations, FoodHub can enhance customer satisfaction, improve operational efficiency, and drive business growth.

# ---
