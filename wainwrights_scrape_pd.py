import pandas as pd
import wikipedia as wp
import os

html = wp.page("List of Wainwrights").html().encode("UTF-8")
df = pd.read_html(html)[1]

# Moving to Data subdirectory using relative filepaths
# Finding absolute path of current file
dirnam = os.path.dirname(os.path.abspath(__file__))
# Joining this to 'Data'
filename = os.path.join(dirnam, 'Data')
# Changing file directory
os.chdir(filename)

df.to_csv('wainwrights_data.csv', header = 0, index = False)
print(df)