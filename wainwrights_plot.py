import matplotlib.pyplot as plt
import pandas
import os

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, 'Data')
os.chdir(filename)

# Setting up data frame with desired columns

df = pandas.read_csv('wainwrights_data.csv', header = None)
df.columns = ["ID","Name","Div","Birkett","Height_metres","Prominence_metres","Height_feet","Prominence_feet","Topo_map","Coords","Class"]
df.drop(labels = ["Div","Birkett","Height_feet","Prominence_feet","Topo_map","Class"], axis = 1, inplace = True)
df["x_coord"] = df["Coords"].str[2:5].astype(int) ; df["y_coord"] = df["Coords"].str[5:8].astype(int)

# If the map used is 'SD', need to take away 1000 from y coord

for row in df.index:
    if str(df.loc[row,"Coords"][0:2]) == 'SD':
        df.loc[row,"y_coord"] = df.loc[row,"y_coord"] - 1000

#



# Plotting the map

os.chdir(dirname)

d1 = min(df["x_coord"]) ; d2 = max(df["x_coord"]) ; d3 = min(df["y_coord"]) ; d4 = max(df["y_coord"])

img = plt.imread("Map.jpg")
fig, ax = plt.subplots()
x = range(300)
ax.imshow(img, extent=[d1, d2, d3, d4])
ax.scatter(x = df['x_coord'],y = df['y_coord'],color='red',marker = 10)
plt.show()