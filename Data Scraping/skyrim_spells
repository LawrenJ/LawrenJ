#Import the pandas library
import pandas as pd
#Get all the tables from url
df = pd.read_html('https://elderscrolls.fandom.com/wiki/Restoration_(Skyrim)')
destruction = pd.read_html('https://elderscrolls.fandom.com/wiki/Destruction_(Skyrim)')
alteration = pd.read_html('https://elderscrolls.fandom.com/wiki/Alteration_(Skyrim)')
conjuration = pd.read_html('https://elderscrolls.fandom.com/wiki/Conjuration_(Skyrim)')
illusion = pd.read_html('https://elderscrolls.fandom.com/wiki/Illusion_(Skyrim)')

#Locate the needed tables
frames = df[1:6]
des = destruction[1:6]
alt = alteration[1:6]
conj = conjuration[1:6]
ill = illusion[1:6]

data = pd.concat(frames)
data_des = pd.concat(des)
data_alt = pd.concat(alt)
data_conj = pd.concat(conj)
data_ill = pd.concat(ill)
print(data)
print(type(data)) 
#Remove the unnecessary columns
cleanData = data.drop(data.columns[[1,2]], axis=1)
print(data)
#Save the collected data to .csv format
data.to_csv('Skyrim1.csv', index=False, header=False)
data_des.to_csv('Destruction.csv', index=False, header=False)
data_alt.to_csv('Alteration.csv', index=False, header=False)
data_conj.to_csv('Conjuration.csv', index=False, header=False)
data_ill.to_csv('Illuson.csv', index=False, header=False)