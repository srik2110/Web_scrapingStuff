from google import search
import pandas as pd

df = pd.read_excel('Report.xlsx')
print df.head()
names = df['Name'].tolist()
needed_links = []
for name in names:
   links = []
   for url in search('%s pharma' %name, num = 1, stop = 1):
      links.append(url)
   #print links
   needed_links.append(links[0])
   print links[0]
df = df.assign(links = pd.Series(needed_links))
#or
#se = pd.Series(needed_links)
#df['Links'] = se.values
df.to_csv('updated.csv')
