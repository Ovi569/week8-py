import pandas as pd

# Import necessary libraries

# Load the OWID COVID-19 dataset (update the path to your actual file location)
# Make sure you have downloaded the latest 'owid-covid-data.csv' from https://ourworldindata.org/covid-deaths
data = pd.read_csv('owid-covid-data.csv')

# Display the first few rows to understand the structure
print("Sample data:")
print(data.head())

# Function to get total deaths for a specific country
def get_total_deaths(country):
    # Filter data for the selected country
    country_data = data[data['location'] == country]
    # Get the latest available total deaths
    latest = country_data['total_deaths'].dropna().max()
    return latest

# Function to get daily deaths for a specific country
def get_daily_deaths(country):
    country_data = data[data['location'] == country]
    # Return date and new_deaths columns
    return country_data[['date', 'new_deaths']].dropna()

# Example usage
country = 'Kenya'  # Change to any country of interest
total_deaths = get_total_deaths(country)
print(f"\nTotal COVID-19 deaths in {country}: {total_deaths}")

daily_deaths = get_daily_deaths(country)
print(f"\nDaily deaths in {country}:")
print(daily_deaths.tail(10))  # Show last 10 days

# NOTES:
# - The dataset is updated frequently; always use the latest version for accurate results.
# - Some countries may have missing data for certain dates.
# - 'total_deaths' and 'new_deaths' columns may contain NaN values; handle with care.
# - You can extend this script to visualize data using matplotlib or seaborn.