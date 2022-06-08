# Description: Demo of web scraping with Selenium.
# Author: Haley Hunter-Zinck
# Date: 2022-06-08
# URL: https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
# note: will need to download chrome driver from https://chromedriver.chromium.org/downloads

import logging
import time

import pandas as pd
from statistics import median, mean

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

tic = time.time()
logging.basicConfig(level=logging.INFO)

outfile = "player_salaries.csv"
df = pd.DataFrame(columns=['Player','Salary','Year']) 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for yr in range(1990,2019):

    logging.info(f"Gathering salaries for year {yr}...")

    page_num = str(yr) + '-' + str(yr+1) +'/'
    url = 'https://hoopshype.com/salaries/players/' + page_num
    driver.get(url)
    
    players = driver.find_elements(by=By.CLASS_NAME, value="name")
    salaries = driver.find_elements(by=By.CLASS_NAME, value="hh-salaries-sorted")
    
    players_list = []
    for p in range(1, len(players), 1):
        players_list.append(players[p].text)
    
    salaries_list = []
    for s in range(1, len(salaries), 1):
        salary_text = salaries[s].text
        salary_int = int(salary_text.replace("$","").replace(",", ""))
        salaries_list.append(salary_int)
    
    data_tuples = list(zip(players_list,salaries_list)) # list of each players name and salary paired together
    temp_df = pd.DataFrame(data_tuples, columns=['Player','Salary']) # creates dataframe of each tuple in list
    temp_df['Year'] = yr # adds season beginning year to each dataframe
    df = pd.concat([df, temp_df]) # appends to master dataframe
    
driver.close()

df.to_csv(outfile, index=False)
logging.info(f"Salaries written to '{outfile}'.")

toc = time.time()
print(f"Runtime: {round(toc - tic)} s")
  