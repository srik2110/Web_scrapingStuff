from Bio import Entrez
from Bio import Medline
import pandas as pd

MAX_COUNT = 300 
#TERM = 'Tuberculosis'
TERM = 'precursor bioink  gelatin'#pubmed has only 2 papers on these key words, google scholar has lot

print('Getting {0} publications containing {1}...'.format(MAX_COUNT, TERM))
Entrez.email = 'A.N.Other@example.com'
h = Entrez.esearch(db='pubmed', retmax=MAX_COUNT, term=TERM)
#h = Entrez.esearch(db='pubmed', term=TERM)

#print (h)
#print (type(h))
result = Entrez.read(h)
#print (result)
#print (type(result))
#print (dir(result))
print('Total number of publications containing {0}: {1}'.format(TERM, result['Count']))
ids = result['IdList']
print (ids)
h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')#handle
#h = Entrez.efetch('pubmed', id=ids, retmode='xml')
#records = Entrez.parse(h)
#print (type(h))
#print (dir(h))
#print (h)
records = Medline.parse(h)
#print (records)
#print (dir(records))
#print (type(records))

#for record in records:
#   print(record)#['AD'])#['Article'])
#h.close()

#authors = []
d = []
for record in records:
#    record: dictionary holding information
   if record.get('FAU') is not None:
       d.append({'Address':record.get('AD'), 'Full_Author':record.get('FAU'), 'Author':record.get('AU'), 'TA':record.get('TA'), 'PMID':record.get('PMID'), 'TI':record.get('TI'), 'PL':record.get('PL'), 'JT':record.get('JT'), 'SO':record.get('SO'), 'PT':record.get('PT'), 'DP':record.get('DP'), 'LA':record.get('FAU')[-1], 'FA':record.get('FAU')[0]})
   elif record.get('AU') is not None:
       d.append({'Address':record.get('AD'), 'Full_Author':record.get('FAU'), 'Author':record.get('AU'), 'TA':record.get('TA'), 'PMID':record.get('PMID'), 'TI':record.get('TI'), 'PL':record.get('PL'), 'JT':record.get('JT'), 'SO':record.get('SO'), 'PT':record.get('PT'), 'DP':record.get('DP'), 'LA':record.get('AU')[-1], 'FA' : record.get('AU')[0]})
   else:
      d.append({'Address':record.get('AD'), 'Full_Author':record.get('FAU'), 'Author':record.get('AU'), 'TA':record.get('TA'), 'PMID':record.get('PMID'), 'TI':record.get('TI'), 'PL':record.get('PL'), 'JT':record.get('JT'), 'SO':record.get('SO'), 'PT':record.get('PT'), 'DP':record.get('DP'), 'LA': None, 'FA' : None})
 


#   print (d)
#'RN':record['RN'], 'OT':record['OT'], 
df1 = pd.DataFrame(d)
df1.to_csv('Test.csv')
#   print (record['AD'])
#    print (record['FAU']['AD'])
#    #each record has all the information about a article in the form a dictionary. So you can get all the information, from the keys of the dictionary.
#    au = record.get('AU', '?')
#    for a in au: 
#        if a not in authors:
#            authors.append(a)
#    authors.sort()
#print('Authors: {0}'.format(', '.join(authors)))


