import sys

import numpy as np
import pandas as pd
from scipy.stats import norm, chisquare, ttest_ind
import matplotlib.pyplot as plt
import datetime


"""
Preamble: Load data from source CSV files 
"""
# Load data by year from 2018 to 2023
path_to_data_folder = "../../data/Weather-Data/"
path_to_2018 = path_to_data_folder + "virginia 2018-01-01 to 2018-12-31.csv"
path_to_2019 = path_to_data_folder + "virginia 2019-01-01 to 2019-12-31.csv"
path_to_2020 = path_to_data_folder + "virginia 2020-01-01 to 2020-12-31.csv"
path_to_2021 = path_to_data_folder + "virginia 2021-01-01 to 2021-12-31.csv"
path_to_2022 = path_to_data_folder + "virginia 2022-01-01 to 2022-12-31.csv"
path_to_2023 = path_to_data_folder + "virginia 2023-01-01 to 2023-12-31.csv"

"""
Question 1: Find the weekly average temperatures for each year and report which week of each year had the lowest and 
highest average temperature. Count the number of weeks where the weekly average temperature was below 50 degrees 
fahrenheit for each year. Print out the year with the most and the year with the least amount of weeks below 50 degrees 
fahrenheit.
"""
print('-----Question 1-----')

def analyze_yearly_data(year, file_path):
    """
    Perform analysis on temperature data to return information on weekly temperature averages
    :param year: year from which the data is from
    :param file_path: path to csv file with temperature data
    :return:
        - dataframe of weekly average temperatures
        - lowest weekly average temperature (float) and its corresponding date (datetime)
        - highest weekly average temperature (float) and its corresponding date (datetime)
        - number of weeks when weekly average temperature was below 50 degrees Fahrenheit (integer)
    """
    # Load the data
    data = pd.read_csv(file_path) # load csv using pandas
    df = pd.DataFrame(data, columns = ['datetime', 'temp']) # Extract the date and temperature columns
    df['datetime'] = pd.to_datetime(df['datetime']) # convert to datetime format to ease reporting

    # filter the data by the given year
    df_year = df[df['datetime'].dt.year == year]

    # Use resample to set 'datetime' as the index to make it easier to report values
    df_year.set_index('datetime', inplace=True)

    # Resample by week (starting on monday) and calculate weekly average temperatures
    weekly_avg = df_year.resample('W-MON').mean()

    low_temp = weekly_avg['temp'].min() # Find the lowest average weekly temperature
    low_index = weekly_avg['temp'].idxmin() # Find date index with the lowest average temperature

    high_temp = weekly_avg['temp'].max() # Find the highest average weekly temperature
    high_index = weekly_avg['temp'].idxmax() # Find the date index with the highest average temperature

    below_50_weeks = (weekly_avg['temp'] < 50).sum() # Count number of weeks below 50 degrees Fahrenheit

    return weekly_avg, low_temp, low_index, high_temp, high_index, below_50_weeks

weekly_avg_2018, low_temp_2018, low_index_2018, high_temp_2018, high_index_2018, below_50_weeks_2018 = analyze_yearly_data(2018, path_to_2018)
weekly_avg_2019, low_temp_2019, low_index_2019, high_temp_2019, high_index_2019, below_50_weeks_2019 = analyze_yearly_data(2019, path_to_2019)
weekly_avg_2020, low_temp_2020, low_index_2020, high_temp_2020, high_index_2020, below_50_weeks_2020 = analyze_yearly_data(2020, path_to_2020)
weekly_avg_2021, low_temp_2021, low_index_2021, high_temp_2021, high_index_2021, below_50_weeks_2021 = analyze_yearly_data(2021, path_to_2021)
weekly_avg_2022, low_temp_2022, low_index_2022, high_temp_2022, high_index_2022, below_50_weeks_2022 = analyze_yearly_data(2022, path_to_2022)
weekly_avg_2023, low_temp_2023, low_index_2023, high_temp_2023, high_index_2023, below_50_weeks_2023 = analyze_yearly_data(2023, path_to_2023)

print("-------------------------------------------------")
print("Year|\t\tLowest Temp|\t\t\tWeek with lowest Temp|\t\tHighest Temp|\t\t\tWeek with highest Temp|\t\tWeeks Below 50")
print("2018", "|\t\t\t", low_temp_2018, "|\t\t\t\t",low_index_2018, "|\t\t", high_temp_2018, "|\t\t",high_index_2018, "|\t", below_50_weeks_2018)
print("2019", "|\t", low_temp_2019, "|\t\t",low_index_2019, "|\t\t", high_temp_2019, "|\t\t",high_index_2019, "|\t", below_50_weeks_2019)
print("2020", "|\t", low_temp_2020, "|\t\t",low_index_2020, "|\t\t", high_temp_2020, "|\t\t",high_index_2020, "|\t", below_50_weeks_2020)
print("2021", "|\t", low_temp_2021, "|\t\t",low_index_2021, "|\t\t", high_temp_2021, "|\t\t",high_index_2021, "|\t", below_50_weeks_2021)
print("2022", "|\t", low_temp_2022, "|\t\t",low_index_2022, "|\t\t", high_temp_2022, "|\t\t",high_index_2022, "|\t", below_50_weeks_2022)
print("2023", "|\t", low_temp_2023, "|\t\t",low_index_2023, "|\t\t", high_temp_2023, "|\t\t",high_index_2023, "|\t", below_50_weeks_2023)
print("-------------------------------------------------")

"""
Question 2: Perform a t-test to determine whether the weekly averages for 2018 and 2023 are equivalent or not. Clearly 
report the p-value for the t-test and make a clear determination as to whether they are equal or not. Calculate the 
temperature error for the dataset where error is expressed as the difference between 2018 and 2023 temperature data. 
Fit this error distribution to a normal curve and plot a histogram of the data on the same plot showing the fitted 
normal curve. Include appropriate labels, titles, and legends. 
"""
print('-----Question 2-----')
# analyze data for 2018 and 2023

# Perform a t-test to compare weekly average between 2018 and 2023
t_test, p_value = ttest_ind(weekly_avg_2018['temp'], weekly_avg_2023['temp'])
print("The p-value is " + str(p_value) + " and the t-test statistic is " + str(t_test))

# Determine if the means are statistically different
alpha = 0.05 # set the alpha value
if p_value < alpha:
    print("The weekly average temperatures for 2018 and 2023 are significantly different")
else:
    print("The weekly average temperatures for 2018 and 2023 are not significantly different")

# Calculate the temperature error between 2018 and 2023
avg_temp_2018 = weekly_avg_2018['temp'].to_numpy() # send to numpy to ease analysis
avg_temp_2023 = weekly_avg_2023['temp'].to_numpy()
temp_error = avg_temp_2018 - avg_temp_2023

(fitted_mean, fitted_std) = norm.fit(temp_error)

plt.hist(temp_error, bins=16, label="Temp Error") # histogram of the data with 16 bins

temp_min = min(temp_error) # use min to find start for linspace
temp_max = max(temp_error) # use max to find stop for linspace
# use lin space to make a vector with a linear spacing of points between start and stop
x_temp = np.linspace(temp_min, temp_max, 100)
temp_pdf = norm.pdf(x_temp, fitted_mean, fitted_std) # use the normal distribution probability density function to generate results
plt.figure(figsize=(8, 6))
plt.plot(x_temp, temp_pdf, label="Normal Curve") # plot the sampled distribution

plt.title("Temp Error Distribution To Fitted Normal Curve")
plt.xlabel("Temp Error")
plt.ylabel("Density")
plt.legend()
plt.show()

# print out the results
print('Parameters for fitted distribution are mu=', fitted_mean, ' and std=', fitted_std)

# determine the 95% confidence interval with scipy
(lower_ci, upper_ci) = norm.interval(confidence=0.95, loc=fitted_mean, scale=fitted_std)

# print out the results
print('For the fitted temp data. The 95% confidence interval is: (', lower_ci, ",", upper_ci, ")")


"""
Question 3: Weather irregularities. Calculate when the weekly average has changed by 50 percent or more week to week.
"""
print('-----Question 3-----')
"""
all_weekly_avg = pd.concat([weekly_avg_2018, weekly_avg_2019,  weekly_avg_2020, weekly_avg_2021, weekly_avg_2022, weekly_avg_2023], axis=0)

all_weekly = all_weekly_avg['temp'].to_numpy()
difference_each_week = np.gradient(all_weekly)
arr = np.array(difference_each_week)
percent_change = np.diff(arr)/arr[:-1]*100
print(percent_change)

# Find the indices where the percentage change is 50% or more
irregularities_indices = np.where(np.abs(percent_change) >= 50)[0]

# Print out the weeks where the change is 50% or more
print("Weeks with 50% or more change in weekly average:")
for idx in irregularities_indices:
    print(f"Week {all_weekly_avg.iloc[idx]['week']}: {percent_change[idx]:.2f}% change")
"""