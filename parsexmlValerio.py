# Importing the required libraries
import xml.etree.ElementTree as ET
import pandas as pd
  
cols = ["Date", "Countries and Territories", "Number of Cases", "Deaths"]
rows = []
  
# Parsing the XML file
xmlparse = ET.parse('/Prelim_Skills_Exam/Covid_cases_xml.xml')
root = xmlparse.getroot()
for i in root:
    date = i.find("dateRep").text
    countries = i.find("countriesAndTerritories").text
    numcases = i.find("cases").text
    death = i.find("deaths").text
  
    rows.append({"date": date,
                 "countries": countries,
                 "numcases": numcases,
                 "death": death})
  
df = pd.DataFrame(rows, columns = cols) 
  
# write dataframe to csv
df.to_csv('final2.csv')
