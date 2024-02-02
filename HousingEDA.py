
# Load libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



housing_data = pd.read_csv(r"C:\Users\shado\OneDrive\Documents\Housing.csv")

housing_data.head(10)

housing_data.info()

print()

housing_data.columns

print()

print(housing_data.describe())

sns.countplot(x = 'bedrooms', data = housing_data)

housing_data.rename(index=str, columns={'price': 'House_Price',
                              'area': 'House_Area',
                              'bedrooms': 'No_Bedrooms',
                              'bathrooms': 'No_Bathrooms',
                              'stories': 'No_Stories',
                              'mainroad': 'On_Mainroad',
                              'guestroom': 'Has_Guestroom',
                              'basement': 'Has_Basement',
                              'hotwaterheating': 'Has_Hot_Hater',
                              'airconditioning': 'is_Air_Conditioned',
                              'parking': 'No_Parking_Spaces',
                              'prefarea': 'in_Pref_Area',
                              'furnishingstatus': 'Type_of_Furnishing'
                              }, inplace=True)

print(housing_data.head())


print()

print("\n Amount of null data")
print(housing_data.isnull().sum())

print()

#Keep first items in data frame if any items are duplicated 
housing_data.duplicated(keep='first')


# Countplot for Number of Bedrooms

sns.catplot(y='No_Bedrooms',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.No_Bedrooms.value_counts().index,
           data=housing_data)


# Countplot for Number of Bathrooms

sns.catplot(y='No_Bathrooms',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.No_Bathrooms.value_counts().index,
           data=housing_data)


# Countplot for Number of Stories in the House

sns.catplot(y='No_Stories',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.No_Stories.value_counts().index,
           data=housing_data)


# Countplot for Mainroad

sns.catplot(y='On_Mainroad',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.On_Mainroad.value_counts().index,
           data=housing_data)


# Countplot for Number of guest rooms
sns.countplot(housing_data['No_Bathrooms'])
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.title('Guestroom Count Plot')

sns.catplot(y='Has_Guestroom',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.Has_Guestroom.value_counts().index,
           data=housing_data)


# Countplot for Basement

sns.catplot(y='Has_Basement',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.Has_Basement.value_counts().index,
           data=housing_data)


# Countplot for Airconditioning

sns.catplot(y='is_Air_Conditioned',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.is_Air_Conditioned.value_counts().index,
           data=housing_data)


# Countplot for Number of Parking Spaces

sns.catplot(y='No_Parking_Spaces',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.No_Parking_Spaces.value_counts().index,
           data=housing_data)

#plt.show()

# Countplot for Preferred Area

sns.catplot(y='in_Pref_Area',
           kind='count',
            height=8, 
            aspect=1.5,
            order=housing_data.in_Pref_Area.value_counts().index,
           data=housing_data)


print(housing_data.groupby(by=['No_Bathrooms'], as_index=False)['House_Price'].count().head())


sns.histplot(housing_data['No_Bathrooms'])


print()

#plt.scatter(df['engine-size'],df['price'])
#plt.xlabel('Engine Size')
#plt.ylabel('Price')
#plt.show()

plt.scatter(housing_data['House_Area'], housing_data['House_Price'])
plt.xlabel('Area of House')
plt.ylabel("Price of House")
plt.show()