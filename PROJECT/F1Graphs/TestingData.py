# Library for opening url and creating requests
import urllib.request
# pretty-print python data structures
from pprint import pprint

# for converting the parsed data in a
# pandas dataframe
import pandas as pd
# for parsing all the tables present on the website
from html_table_parser import HTMLTableParser


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
pprint(p.tables[0])

# converting the parsed data to dataframe
#print("\n\nPANDAS DATAFRAME\n")
print(pd.DataFrame(p.tables[1]))
