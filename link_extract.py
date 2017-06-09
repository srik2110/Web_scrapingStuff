#import urllib
#link = "http://pubs.acs.org/doi/abs/10.1021/acsami.7b00849"
#f = urllib.urlopen(link)
#myfile = f.read()
#print myfile


#########or
import requests
link = "http://pubs.acs.org/doi/abs/10.1021/acsami.7b00849"


#query the website and return the request to the variable page
page = requests.get(link)

#print page.text

#import the beautiful soup functions to parse the data returned from the website

from bs4 import BeautifulSoup

#parse the html in the 'page.text' variable and store it in the Beutiful Soup format
soup = BeautifulSoup(page.text)
#print soup.prettify()
title = soup.find("meta", {'name':'dc.Title'})
#print title['content']
authors = soup.findAll("meta", {'name':'dc.Creator'})
list_auth = []
for author in authors:
    list_auth.append(author['content'])	
#print authors
publisher = soup.find('meta', {'name':'dc.Publisher'})
pub_year = soup.find('meta', {'name':'dc.Date'})
#affiliations
affs = soup.find('div', {"class":"affiliations"})
#print affs.text
#citation
div = soup.find('div', {'id':'citation'})
cite = div.find('cite')

#keep appending to a list of details of all the links
Title = []
Authors = []
Publisher = []
Year = []
Affiliations = []
Journal = []
Title.append(title['content'])
Authors.append(list_auth)
Publisher.append(publisher['content'])
Year.append(pub_year['content'])
Affiliations.append(affs.text.encode('utf-8'))
Journal.append(cite.text)

#convert list to data frame
import pandas as pd
df = pd.DataFrame(Title, columns = ['Title'])
df['Authors'] = Authors
df['Publisher'] = Publisher
df['Year'] = Year
df['Affiliations'] = Affiliations
df['Journal'] = Journal
#print df
df.to_csv('Test_link.csv')


