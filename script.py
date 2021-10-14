import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Print the first few of london_data
print(london_data.head())

#print(london_data.iloc[100:200])

# Print the length of london_data
print(len(london_data))

# Set "TemperatureC" column of london_data to the variable temp
temp = london_data["TemperatureC"]

# Find the average temperature in London in 2015
average_temp = np.average(temp)

# Calculate the varience of temp
temperature_var = np.var(temp)

# Print average_temp
print(average_temp)

# Print temperature_var
print(temperature_var)

# Calculate standard deviation of temp
temperature_standard_deviation = np.std(temp)

# Print temperature_standard_deviation
print(temperature_standard_deviation)

# Print the first few of london_data
print(london_data.head())

# View the end of london_data
print(london_data.tail())

# Create a variable called june that gets the temperature from the rows where "month" is 6
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

# Create a variable called july that gets the temperature from the rows where "month" is 7
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

# Output the average temperature in June from london_data
print(np.mean(june))

# Output the average temperature in July from london_data
print(np.mean(july))

# Calculate and print the standard deviation of temperature in London for June
print(np.std(june))

# Calculate and print the standard deviation of temperature in London for July
print(np.std(july))

# Print the mean and standard deviatio of every month in London for temperature
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# Print the mean and standard deviation of every month in London for humidity
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["Humidity"]
  print("The mean humidity in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of humidity in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# Print out the unique data of "hour" column from the dataset, london_data
print(london_data.hour.unique())

# Check the mean and standard Deviation of every hour for temperature
for i in range(24):
  hour = london_data.loc[london_data["hour"] == i]["TemperatureC"]
  print("The mean temperature in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation of temperature in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")

# Check the mean and standard Deviation of every hour for humidity
for i in range(24):
  hour = london_data.loc[london_data["hour"] == i]["Humidity"]
  print("The mean humidity in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation of humidity in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")