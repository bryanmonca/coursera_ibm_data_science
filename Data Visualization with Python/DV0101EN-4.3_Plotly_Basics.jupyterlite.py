#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/labs/Module%204/logo.png" width="300" alt="cognitiveclass.ai logo">
# </center>
# 

# # Basic Plotly Charts
# 
# Estimated time needed: 45 minutes
# 

# # Objectives
# 
# 
# After completing this lab, you will be able to:
# 
# *   Use plotly graph objects and plotly express libraries to plot different types of charts
# *   Create interesting visualizations on Airline Reporting Carrier On-Time Performance Dataset 
# 

# # Plotly graph objects and Plotly express libraries to plot different types of charts 
# 
# ## Plotly Libraries
# 
# **plotly.graph_objects:** 
# This is a low level interface to figures, traces and layout. The Plotly graph objects module provides an automatically generated hierarchy of classes ( figures, traces, and layout) called graph objects. These graph objects represent figures with a top-level class plotly.graph_objects.Figure.
# 
# **plotly.express:** 
# Plotly express is a high-level wrapper for Plotly. It is a recommended starting point for creating the most common figures provided by Plotly using a simpler syntax. It uses graph objects internally.
# Now let us use these libraries to plot some charts
# We will start with plotly_graph_objects to plot line and scatter plots
# > Note: You can hover the mouse over the charts whenever you want to view any statistics in the visualization charts 
# 
# 
# 
# 
# ## Exercise I: Get Started with Different Chart types in Plotly
# 

# In[1]:


import piplite

await piplite.install(['nbformat', 'plotly'])


# In[2]:


# Import required libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# ## 1. Scatter Plot: 
# A scatter plot shows the relationship between 2 variables on the x and y-axis. The data points here appear scattered when plotted on a two-dimensional plane. Using scatter plots, we can create exciting visualizations to express various relationships, such as:
# 
# * Height vs weight of persons
# * Engine size vs automobile price
# * Exercise time vs Body Fat
# 

# In[3]:


##Example 1: Let us illustrate the income vs age of people in a scatter plot

age_array=np.random.randint(25,55,60)
# Define an array containing salesamount values 
income_array=np.random.randint(300000,700000,3000000)


# In[4]:


##First we will create an empty figure using go.Figure()
fig=go.Figure()
fig


# In[5]:


#Next we will create a scatter plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data,y-axis data and define the mode as markers with color of the marker as blue
fig.add_trace(go.Scatter(x=age_array, y=income_array, mode='markers', marker=dict(color='blue')))


# **However in the previous output title, x-axis and y-axis labels are missing. Let us use the update_layout function to update the title and labels.**
# 

# In[6]:


## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Economic Survey', xaxis_title='Age', yaxis_title='Income')
# Display the figure
fig.show()


# #### Inferences:
#      
# From the above plot we find that the Income of a person is not correlated with age. We find that as the age increases the income may or not decrease.
# 

# ## 2. Line Plot: 
# A line plot shows information that changes continuously with time. Here the data points are connected by straight lines. Line plots are also plotted on a two dimensional plane like scatter plots. Using line plots, we can create exciting visualizations to illustrate:
# 
#   * Annual revenue growth
#   * Stock Market analysis over time
#   * Product Sales over time
# 

# In[7]:


##Example 2: Let us illustrate the sales of bicycles from Jan to August last year using a line chart
# Define an array containing numberofbicyclessold  
numberofbicyclessold_array=[50,100,40,150,160,70,60,45]
# Define an array containing months
months_array=["Jan","Feb","Mar","April","May","June","July","August"]


# In[8]:


##First we will create an empty figure using go.Figure()
fig=go.Figure()


# In[9]:


#Next we will create a line plot by using the add_trace function and use the go.scatter() function within it
# In go.Scatter we define the x-axis data,y-axis data and define the mode as lines with color of the marker as green
fig.add_trace(go.Scatter(x=months_array, y=numberofbicyclessold_array, mode='lines', marker=dict(color='green')))


# In[10]:


## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')
# Display the figure
fig.show()


# #### Inferences:
#      
# From the above plot we find that the sales is the highest in the month of May and then there is a decline in sales.
# 

# We will now use plotly express library to plot the other graphs
# 

#   
# ## 3.Bar Plot: 
# A bar plot represents categorical data in rectangular bars. Each category is defined on one axis, and the value counts for this category are represented on another axis. Bar charts are generally used to compare values.We can use bar plots in visualizing:
# 
#  * Pizza delivery time in peak and non peak hours
#  * Population comparison by gender
#  * Number of views by movie name
# 

# In[11]:


##Example 3: Let us illustrate the average pass percentage of classes from grade 6 to grade 10

# Define an array containing scores of students 
score_array=[80,90,56,88,95]
# Define an array containing Grade names  
grade_array=['Grade 6','Grade 7','Grade 8','Grade 9','Grade 10']


# **In plotly express we set the axis values and the title within the same function call `px.<graphtype>(x=<xaxis value source>,y=<y-axis value source>,title=<appropriate title as a string>)`.In the below code we use `px.bar( x=grade_array, y=score_array, title='Pass Percentage of Classes')`.**
# 

# In[12]:


# Use plotly express bar chart function px.bar.Provide input data, x and y axis variable, and title of the chart.
# This will give average pass percentage per class
fig = px.bar( x=grade_array, y=score_array, title='Pass Percentage of Classes') 
fig.show()


# #### Inferences:
#      
# From the above plot we find that Grade 8 has the lowest pass percentage and Grade 10 has the highest pass percentage 
# 

# 
# ## 4.Histogram: 
#  A histogram is used to represent continuous data in the form of bar. Each bar has discrete values in bar graphs, whereas in histograms, we have bars representing a range of values. Histograms show frequency distributions. We can use histograms to visualize:
#  
#  * Students marks distribution
#  * Frequency of waiting time of customers in a Bank
# 

# In[13]:


##Example 4: Let us illustrate the distribution of heights of 200 people using a histogram

import numpy as np
#Here we will concentrate on heights which are 160 and the standard deviation is 11
heights_array = np.random.normal(160, 11, 200)
## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
fig = px.histogram(x=heights_array,title="Distribution of Heights")
fig.show()


# #### Inferences
# From this we can analyze that there are around 
# 2 people who are at the height of 130cm and 45 people at the height of 160 cm
# 

# ## 5. Bubble Plot: 
# A bubble plot is used to show the relationship between 3 or more variables. It is an extension of a scatter plot. Bubble plots are ideal for visualizing:
# 
#   * Global Economic position of Industries
#   * Impact of viruses on Diseases
# 

# In[14]:


##Example 4: Let us illustrate crime statistics of US cities with a bubble chart

#Create a dictionary having city,numberofcrimes and year as 3 keys
crime_details = {
    'City' : ['Chicago', 'Chicago', 'Austin', 'Austin','Seattle','Seattle'],
    'Numberofcrimes' : [1000, 1200, 400, 700,350,1500],
    'Year' : ['2007', '2008', '2007', '2008','2007','2008'],
}
  
# create a Dataframe object with the dictionary
df = pd.DataFrame(crime_details)
  
df


# In[15]:


## Group the number of crimes by city and find the total number of crimes per city
bub_data = df.groupby('City')['Numberofcrimes'].sum().reset_index()


# In[16]:


##Display the grouped dataframe
bub_data


# In[17]:


## Bubble chart using px.scatter function with x ,y and size varibles defined.Title defined as Crime Statistics
fig = px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",
                 hover_name="City", title='Crime Statistics', size_max=60)
fig.show()


# #### Inferences
# The size of the bubble in the bubble chart indicates that Chicago has the highest crime rate when compared with the other 2 cities.
# 

#  ## 6.Pie Plot: 
#  A pie plot is a circle chart mainly used to represent proportion of part of given data with respect to the whole data. Each slice represents a proportion and on total of the proportion becomes a whole. We can use bar plots in visualizing:
#  
#  * Sales turnover percentatge with respect to different products
#  * Monthly expenditure of a Family
# 

# In[18]:


## Monthly expenditure of a family
# Random Data
exp_percent= [20, 50, 10,8,12]
house_holdcategories = ['Grocery', 'Rent', 'School Fees','Transport','Savings']


# In[19]:


# Use px.pie function to create the chart. Input dataset. 
# Values parameter will set values associated to the sector. 'exp_percent' feature is passed to it.
# labels for the sector are passed to the `house hold categoris` parameter.
fig = px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenditure')
fig.show()


# #### Inferences
# From this pie chart we can find that the family expenditure is maximum for rent.
# 

# ## 7.Sunburst Charts: 
# Sunburst charts represent hierarchial data in the form of concentric circles. Here the innermost circle is the root node which defines the parent, and then the outer rings move down the hierarchy from the centre. They are also called radial charts.We can use them to plot
# 
# * Worldwide mobile Sales where we can drill down as follows:   
#     * innermost circle represents total sales  
#     * first outer circle represents continentwise sales
#     * second outer circle represents countrywise sales within each continent
#     
#     
# * Disease outbreak hierarchy
# 
# 
# * Real Estate Industrial chain
# 

# In[20]:


##Example 4: Let us illustrate plot the 

#Create a dictionary having a set of people represented by a character array and the parents of these characters represented in another
## array and the values are the values associated to the vectors.
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig = px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
    title="Family chart"
)
fig.show()


# #### Inferences
# 
# It is found that here the innermost circle **Eve** represents the parent and the second outer circle represents his childrent **Cain**,**Seth** and so on.Further the outermost circle represents his grandchildren **Enoch** and **Enos**
# 

# ## II- Practice Exercises: Apply your Plotly Skills to an Airline Dataset
# 
# The Reporting Carrier On-Time Performance Dataset contains information on approximately 200 million domestic US flights reported to the United States Bureau of Transportation Statistics. The dataset contains basic information about each flight (such as date, time, departure airport, arrival airport) and, if applicable, the amount of time the flight was delayed and information about the reason for the delay. This dataset can be used to predict the likelihood of a flight arriving on time.
# 
# Preview data, dataset metadata, and data glossary [here.](https://dax-cdn.cdn.appdomain.cloud/dax-airline/1.0.1/data-preview/index.html)
# 

# # Read Data
# 

# In[21]:


# Read the airline data into pandas dataframe
from js import fetch
import io

URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
resp = await fetch(URL)
text = io.BytesIO((await resp.arrayBuffer()).to_py())

airline_data =  pd.read_csv(text,
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

print('Data downloaded and read into a dataframe!')


# In[22]:


# Preview the first 5 lines of the loaded data 
airline_data.head()


# In[23]:


# Shape of the data
airline_data.shape


# In[24]:


# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)


# In[25]:


# Get the shape of the trimmed data
data.shape


# It would be interesting if we visually  capture details such as
# 
# * Departure time changes with respect to airport distance.
# 
# * Average Flight Delay time over the months
# 
# * Comparing number of flights in each destination state
# 
# * Number of  flights per reporting airline
# 
# * Distrubution of arrival delay
# 
# * Proportion of distance group by month (month indicated by numbers)
# 
# * Hierarchical view in othe order of month and destination state holding value of number of flights
# 

# # plotly.graph_objects¶
# 

# ## 1. Scatter Plot
# 

# Let us use a scatter plot to represent departure time changes with respect to airport distance
# 
# This plot should contain the following
# 
# * Title as **Distance vs Departure Time**.
# * x-axis label should be **Distance**
# * y-axis label should be **DeptTime**
# * **Distance** column data from the flight delay dataset should be considered in x-axis
# * **DepTime** column data from the flight delay dataset should be considered in y-axis
# * Scatter plot markers should be of red color
# 

# In[26]:


## Write your code here
fig=go.Figure()
fig.add_trace(go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DeptTime')
fig.show()


# Double-
# click **here** for hint.
# <!-- 
# ***Use go.scatter() method*** and mode as markers
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
#     
# ##First we will create an empty figure ising go.Figure()
# fig=go.Figure()
# #Next we will create a scatter plot by using the add_trace function and use the go.scatter() function within it
# # In go.Scatter we define the x-axis data,y-axis data and define the mode as markers with color of the marker as red
# fig.add_trace(go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))
# fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')
# # Display the figure
# fig.show()
# -->
# 

# #### Inferences
# 
# It can be inferred that there are more flights round the clock for shorter distances. However, for longer distance there are limited flights through the day.
# 

# ## 2. Line Plot
# 

# Let us now use a line plot to extract average monthly arrival delay time and see how it changes over the year.
# 
#   This plot should contain the following
# 
# * Title as **Month vs Average Flight Delay Time**.
# * x-axis label should be **Month**
# * y-axis label should be **ArrDelay**
# * A new dataframe **line_data** should be created which consists of 2 columns average **arrival delay time per month** and **month** from the dataset
# * **Month** column data from the line_data dataframe should be considered in x-axis
# * **ArrDelay** column data from the ine_data dataframeshould be considered in y-axis
# * Plotted line in the line plot should be of green color
# 

# In[27]:


# Group the data by Month and compute average over arrival delay time.
line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()


# In[28]:


# Display the data
line_data


# In[29]:


## Write your code here
fig = go.Figure()
fig.add_trace(go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
fig.show()


# Double-click **here** for hint.
# <!--
# *   Hint: Scatter and line plot vary by updating mode parameter.
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
#     
# ##First we will create an empty figure ising go.Figure()
# fig=go.Figure()
# ##Next we will create a line plot by using the add_trace function and use the go.scatter() function within it
# # In go.Scatter we define the x-axis data,y-axis data and define the mode as lines with color of the marker as green
# fig.add_trace(go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
# # Create line plot here
# ## Here we update these values under function attributes such as title,xaxis_title and yaxis_title
# fig.update_layout(title='Month vs Average Flight Delay Time', xaxis_title='Month', yaxis_title='ArrDelay')
# fig.show()
# -->
# 

# #### Inferences
# 
# It is found that in the month of June the average monthly delay time is the maximum
# 

# # plotly.express¶
# 

# ## 3. Bar Chart
# 

# 
# Let us use a bar chart to extract number of flights from a specific airline that goes to a destination
# 
# This plot should contain the following
# 
# * Title as **Total number of flights to the destination state split by reporting air**.
# * x-axis label should be **DestState**
# * y-axis label should be **Flights**
# * Create a new dataframe called **bar_data**  which contains 2 columns **DestState** and **Flights**.Here **flights** indicate total number of flights in each combination.
# 

# In[30]:


# Group the data by destination state and reporting airline. Compute total number of flights in each combination
bar_data = data.groupby('DestState')['Flights'].sum().reset_index()


# In[31]:


# Display the data
bar_data


# In[32]:


## Write your code here
fig = px.bar(bar_data, x='DestState', y='Flights', title='Total number of flights to the destination state split by reporting air') 
fig.show()


# Double-click **here** for hint.
# <!--
# ***Use the px.bar() function***
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# 
#     
# # Use plotly express bar chart function px.bar. Provide input data, x and y axis variable, and title of the chart.
# # This will give total number of flights to the destination state.
# fig = px.bar(bar_data, x="DestState", y="Flights", title='Total number of flights to the destination state split by reporting airline') 
# fig.show()
# -->
# 

# #### Inferences
# 
# It is found that maximum flights are to destination state **CA** which is around 68 and there is only 1 flight to destination state **VT**
# 

# ## 4. Histogram
# 

# 
# Let us represent the distribution of arrival delay using a histogram
# 
# This plot should contain the following
# 
# * Title as **Total number of flights to the destination state split by reporting air**.
# * x-axis label should be **ArrayDelay**
# * y-axis will show the count of arrival delay
# 

# In[33]:


# Set missing values to 0
data['ArrDelay'] = data['ArrDelay'].fillna(0)


# In[34]:


## Write your code here
fig = px.histogram(data, x='ArrDelay',title="Total number of flights to the destination state split by reporting air")
fig.show()


# Double-click **here** for hint.
# <!--
# ***Use the px.histogram() function***
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ## Use plotly express histogram chart function px.histogram.Provide input data x to the histogram
# fig = px.histogram(data, x="ArrDelay",title="Total number of flights to the destination state split by reporting air.")
# fig.show()
#     
# 
# -->
# 

# #### Inferences
# 
# It is found that there is only max of 5 flights with an arrival delay of 50-54 minutes and around 17 flights with an arrival delay of 20-25 minutes
# 

# ## 5. Bubble Chart
# 

# Let  use a bubble plot to represent number of flights as per reporting airline
# 
# This plot should contain the following
# 
# * Title as **Reporting Airline vs Number of Flights**.
# * x-axis label should be **Reporting_Airline**
# * y-axis label should be **Flights**
# * size of the bubble should be **Flights** indicating number of flights
# * Name of the hover tooltip to `reporting_airline` using `hover_name` parameter.
# 

# In[35]:


# Group the data by reporting airline and get number of flights
bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()


# In[36]:


bub_data


# In[38]:


## Write your code here
fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                 hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
fig.show()


# Double-click **here** for hint.
# <!--
# ***Use the px.scatter() function and define the size attribute values apart from x and y attribute values***
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ## Bubble chart using px.scatter function with x ,y and size variables defined.Title defined as Reporting Airline vs Number of Flights
# fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
#                  hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
# fig.show()
#     
# 
# -->
# 

# #### Inferences
# 
# It is found that the reporting airline **WN** has the highest number of flights which is around 86
# 

# ## 6. Pie Chart
# 

# Let us represent the proportion of distance group by month (month indicated by numbers)
# 
# This plot should contain the following
# 
# * Title as **Distance group proportion by month**.
# * values should be **Month**
# * names should be **DistanceGroup**
# 

# In[39]:


## Write your code here
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()


# Double-click **here** for hint.
# <!--
# ***Use the px.pie() function***
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# # Use px.pie function to create the chart. Input dataset. 
# # Values parameter will set values associated to the sector. 'Month' feature is passed to it.
# # labels for the sector are passed to the `names` parameter.
# fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
# fig.show()
#     
# 
# -->
# 

# #### Inferences
# 
# It is found that February month has the highest distance group proportion
# 

# ## 7. SunBurst Charts
# 

# Let us represent the hierarchical view in othe order of month and destination state holding value of number of flights
# 
# This plot should contain the following
# 
# *  Define hierarchy of sectors from root to leaves in `path` parameter. Here, we go from `Month` to `DestStateName` feature.
# *   Set sector values in `values` parameter. Here, we can pass in `Flights` feature.
# *   Show the figure.
# *   Title as **Flight Distribution Hierarchy**
# 

# In[43]:


## Write your code here
fig = px.sunburst(
    data,
    path=['Month','DestStateName'],
    values='Flights',
    title="Flight Distribution Hierarchy"
)
fig.show()


# Double-click **here** for hint.
# <!--
# ***Use the px.sunburst() function***
# -->
# 

# Double-click **here** for the solution.
# 
# <!-- The answer is below:
# ## Define path as Month and DestStateName and values as Flights.
# fig = px.sunburst(data, path=['Month', 'DestStateName'], values='Flights',title='Flight Distribution Hierarchy')
# fig.show()
#     
# 
# -->
# 

# #### Inferences
# 
# Here the  **Month** numbers present in the innermost concentric circle is the root and for each month we will check the **number of flights** for the different **destination states** under it.
# 

# ## Summary
# 
# Congratulations for completing your lab.
# 
# In this lab, you have learnt how to use `plotly.graph_objects` and `plotly.express` for creating plots and charts.
# 

# ## Author(s)
# [Saishruthi Swaminathan](https://www.linkedin.com/in/saishruthi-swaminathan/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDV0101ENSkillsNetwork970-2022-01-01)
# 
# Lakshmi Holla
# 

# ## Other Contributor(s)
# 
# Lavanya T S
# 

# ## Changelog
# 
# | Date       | Version | Changed by | Change Description                   |
# | ---------- | ------- | ---------- | ------------------------------------ |
# | 12-18-2020 | 1.0     | Nayef      | Added dataset link and upload to Git |
# | 07-02-2023 | 1.1     | Lakshmi Holla     | Updated lab |
# 

# ## <h3 align="center"> © IBM Corporation 2023. All rights reserved. <h3/>
# 
