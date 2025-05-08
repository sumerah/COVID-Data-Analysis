import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Make directory to save generated plots (if directory doesnt exist already)
os.makedirs('output', exist_ok=True)

#Using public dataset from our world in data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)
#Filter for canada
country = "Canada"
df_country = df[df['location'] == country].copy()
df_country['date'] = pd.to_datetime(df_country['date'])

df_plot = df_country[['date', 'new_cases', 'new_deaths']].fillna(0)
df_plot['cases_avg'] = df_plot['new_cases'].rolling(window=7).mean()
df_plot['deaths_avg'] = df_plot['new_deaths'].rolling(window=7).mean()

#Plotting
plt.figure(figsize=(14, 7))

#New Cases
plt.subplot(2, 1, 1)
plt.plot(df_plot['date'], df_plot['new_cases'], label='Daily New Cases', color='lightblue')
plt.plot(df_plot['date'], df_plot['cases_avg'], label='7-Day Avg', color='blue')
plt.title(f'COVID-19 Daily New Cases in {country}')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.legend()

#New Deaths
plt.subplot(2, 1, 2)
plt.plot(df_plot['date'], df_plot['new_deaths'], label='Daily New Deaths', color='lightcoral')
plt.plot(df_plot['date'], df_plot['deaths_avg'], label='7-Day Avg', color='red')
plt.title(f'COVID-19 Daily New Deaths in {country}')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.legend()

plt.tight_layout()
plt.savefig(f'output/covid_trends_{country.lower().replace(" ", "_")}.png')
plt.show()
