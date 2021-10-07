# Importing the required libraries
import xml.etree.ElementTree as ET
import pandas as pd
  
cols = ["dateRep", "countriesAndTerritories", "cases", "death"]
rows = []
  
# Parsing the XML file
xmlparse = ET.parse('covid_cases_xml.xml')
root = xmlparse.getroot()
for i in root:
    date = i.find("dateRep").text
    countries = i.find("countriesAndTerritories").text
    numcases = i.find("cases").text
    death = i.find("deaths").text
  
    rows.append({"dateRep": date,
                 "countriesAndTerritories": countries,
                 "cases": numcases,
                 "death": death})
  

df = pd.DataFrame(rows, columns = cols) 
  
#write dataframe to csv
df.to_csv('final2.csv')
