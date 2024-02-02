import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

median_household = pd.read_csv(r"C:\Users\shado\OneDrive\Desktop\VS Code Code\LawrenJ\Project_1\Data\Median Household Income by County 2011-2021_3.csv")
#print(median_household)


household = median_household.to_numpy
print(household)


table_10 = pd.read_excel(r"C:\Users\shado\OneDrive\Desktop\VS Code Code\LawrenJ\Project_1\Data\table_10_offenses_known_to_law_enforcement_south_carolina_by_metropolitan_and_nonmetropolitan_counties_2012.xls")
offenses_2012 = table_10.to_numpy
print(offenses_2012)

#df.describe()
#plt.sc
#plt.scatter(df['Population'], df['Violent'])
#plt.ylabel('Petal width (cm)')
#plt.xlabel('Petal length (cm)')
#plt.show()
