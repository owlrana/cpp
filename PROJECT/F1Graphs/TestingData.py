import urllib.request
from html_table_parser import HTMLTableParser
import ssl
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl.workbook import Workbook
# Read website content
def url_get_contents(url):

	# Opens a website and read its
	# binary contents (HTTP Response Body)
    context = ssl._create_unverified_context() 
	#making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req, context=context)
    return f.read()

# return racing data table
def dataInitialisation():
    xhtml = url_get_contents('https://www.racefans.net/2021/04/18/2021-emilia-romagna-grand-prix-interactive-data-lap-charts-times-and-tyres/').decode('utf-8')
    p = HTMLTableParser()
    p.feed(xhtml)
    raceData = p.tables[1]
    
    df = pd.DataFrame(raceData)
    df.to_csv("output.csv")  
    df_racingdata = pd.read_csv("output.csv")
    print(df_racingdata)
dataInitialisation()
