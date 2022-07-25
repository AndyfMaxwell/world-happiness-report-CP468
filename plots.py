import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

country_data = pd.read_csv(".\world-happiness-report-2021.csv")

gdp = country_data['Logged GDP per capita']
social = country_data['Social support']
healthy = country_data['Healthy life expectancy']
freedom = country_data['Freedom to make life choices']
generosity = country_data['Generosity']
corruption = country_data['Perceptions of corruption']

ladder = country_data['Ladder score']

fig = plt.figure()

#Uncomment to view plots

# plt.scatter(gdp,ladder)
# plt.xlabel('GDP')

# plt.scatter(social,ladder)
# plt.xlabel('Social')

# plt.scatter(healthy,ladder)
# plt.xlabel('Healthy')

# plt.scatter(freedom,ladder)
# plt.xlabel('Freedom')

# plt.scatter(generosity,ladder)
# plt.xlabel('Generosity')

# plt.scatter(corruption,ladder)
# plt.xlabel('Corruption')

plt.ylabel('Ladder Score')

plt.show()