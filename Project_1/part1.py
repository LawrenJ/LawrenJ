import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#to ignore warnings
import warnings
warnings.filterwarnings('ignore')

housing_est = pd.read_csv("Data\Estimated Number of Housing Units 2010-2019 (1).csv",encoding = 'latin1' )

for col in housing_est:
    print(col)



#df.describe()
#plt.sc
#plt.scatter(df['Population'], df['Violent'])
#plt.ylabel('Petal width (cm)')
#plt.xlabel('Petal length (cm)')
#plt.show()
