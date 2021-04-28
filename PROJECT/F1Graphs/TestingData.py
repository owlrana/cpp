# Library for opening url and creating requests
import urllib.request
# pretty-print python data structures
from pprint import pprint

# for converting the parsed data in a
# pandas dataframe
import pandas as pd
# for parsing all the tables present on the website
from html_table_parser import HTMLTableParser

from matplotlib import pyplot as plt

# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):

    # Opens a website and read its
    # binary contents (HTTP Response Body)

    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    #reading contents of the website
    return f.read()

# defining the html contents of a URL.
xhtml = url_get_contents('https://www.racefans.net/2021/04/18/2021-emilia-romagna-grand-prix-interactive-data-lap-charts-times-and-tyres/').decode('utf-8')

# Defining the HTMLTableParser object
p = HTMLTableParser()

# feeding the html contents in the HTMLTableParser object
p.feed(xhtml)

# Now finally obtaining the data of the table required
#pprint(p.tables[1])
race_table = p.tables[1]

timings = list()
names = list()

for i in range(1, len(race_table)):
    time = race_table[i][3].split()
    try:
        timings.append(int(time[0])*60 + float(time[1])) 
        race_table[i][3] = int(time[0])*60 + float(time[1])
    except:
        timings.append(0)

for i in range(1, len(race_table)):
    names.append(race_table[i][1])

data = list()
data.append(names)
data.append(timings)

for name, time in zip(names, timings):
    print(name, " --> ", time)

plt.bar(names, timings)
plt.show()

#print(race_table)

# converting the parsed data to dataframe
#print("\n\nPANDAS DATAFRAME\n")
#print(pd.DataFrame(p.tables[1]))
