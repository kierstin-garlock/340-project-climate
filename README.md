# 340-project-climate
Engineering Design and Analysis Final Project on Climate Change Data 

# **Abstract**
This project is designed to analyze weather data in order to help address questions related to climate change. The 
questions used to address this topic are listed below. The data used in our analysis is located in the climate 
data folder and includes data from 2003, 2013, and 2018-2023. Question 1 uses a definition to walk through each 
data set and return the desired values, including weeks with the highest and lowest temperature values. Question
2 is a statistical analysis that uses a t-test to determine if there is a significant difference in weekly averages 
between 2018 and 2023. Question 2 also return a plot displaying the error distribution to a normal curve and a 
histogram of the data. Question 3 is designed to try to identify irregularities in temperatures between weeks. To 
improve the analysis of this code, one might increase the range of years from which data was taken. 

# **Questions**
Question 1: Find the weekly average temperatures for each year and report which week of each year had the lowest and 
highest average temperature. Count the number of weeks where the weekly average temperature was below 50 degrees 
fahrenheit for each year.

Question 2: Perform a t-test to determine whether the weekly averages for 2018 and 2023 are equivalent or not. Clearly 
report the p-value for the t-test and make a clear determination as to whether they are equal or not. Calculate the 
temperature error for the dataset where error is expressed as the difference between 2018 and 2023 temperature data. 
Fit this error distribution to a normal curve and plot a histogram of the data on the same plot showing the fitted 
normal curve. Include appropriate labels, titles, and legends.

Question 3: Calculate when the weekly average has changed by 20 percent or more week to week.

# **Code Resources**
| Function Used  | Explination          | Link |  
| :-------------: |:------------------------:| :-----:|
| pd.to_datetime      | convert date column to datetime | https://stackoverflow.com/questions/17087314/get-date-from-week-number |
| dt.year      | filter the data by the given year |  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html  |
| .set_index | Use resample to set 'datetime' as the index to make it easier to report values | https://stackoverflow.com/questions/38542419/could-pandas-use-column-as-index |
| resample('W-MON').mean() | resample data by week starting on monday | https://stackoverflow.com/questions/14530556/resample-time-series-in-pandas-to-a-weekly-interval |
| ttest_ind | Performs t-test for two independent data sets | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html |
| np.linspace | make a vector with a linear spacing of points between start and stop | https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html | 
| norm.pdf | normal distribution probability density function to generate results | https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html | 
| pd.concat | Used to combine data frames along axis | https://pandas.pydata.org/docs/reference/api/pandas.concat.html | 
| np.gradient | Used to compute differences between weeks | https://numpy.org/doc/2.1/reference/generated/numpy.gradient.html | 
| np.where(np.abs()) | Uses “where” to select element and “abs” to return absolute value of element | https://numpy.org/doc/2.1/reference/generated/numpy.where.html | 







