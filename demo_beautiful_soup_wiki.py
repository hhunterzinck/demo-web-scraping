# Description: Scrape wikipedia with Beautiful Soup
# Date: 2022-06-09
# Tutorial: https://towardsdatascience.com/step-by-step-tutorial-web-scraping-wikipedia-with-beautifulsoup-48d7f2dfa52d
# conda env: bs4

import time
import re

import numpy as np
import pandas as pd

import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

df_daly = pd.DataFrame(columns=["country", "daly"]) 
df_precip = pd.DataFrame(columns=["country", "precip"]) 

def process_num(num):
    num_str = re.sub(r"[^\w\s.]","",num)
    if (num_str== "NA"):
        return np.nan
    return float(num_str)

url_daly = "https://en.wikipedia.org/wiki/Epidemiology_of_depression"
url_precip = "https://en.wikipedia.org/wiki/List_of_countries_by_average_annual_precipitation"
soup_daly = BeautifulSoup(urlopen(url_daly).read().decode("utf-8"), "html.parser")
soup_precip = BeautifulSoup(urlopen(url_precip).read().decode("utf-8"), "html.parser")

table_daly = soup_daly.find_all("table")[0]
rows = table_daly.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    
    if len(cells) > 1:

        daly = process_num(cells[2].text.strip())
        country = cells[0].text.strip()

        df_row = pd.DataFrame([[country, daly]], columns=["country", "daly"])
        df_daly = pd.concat([df_daly, df_row])

print(df_daly)

table_precip = soup_precip.find_all("table")[0]
rows = table_precip.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    
    if len(cells) > 1:

        precip = process_num(cells[2].text.strip())
        country = cells[1].text.strip()

        df_row = pd.DataFrame([[country, precip]], columns=["country", "precip"])
        df_precip = pd.concat([df_precip, df_row])

print(df_precip)

df_res = df_daly.join(df_precip, on="country", how="inner")
print(df_res)

