# Description: Handle interactive HTML sites with MechanicalSoup
# Author: Haley Hunter-Zinck
# Date: 2022-06-01
# Tutorial: https://realpython.com/python-web-scraping-practical-introduction/

from mechanicalsoup import Browser
import re
import time

url = "http://olympus.realpython.org/dice"

browser = Browser()
page = browser.get(url)
html = page.soup
print(html)

#pattern = ">[1-6]<"
#str = re.search(pattern, str(html)).group()
#digit = re.sub("[<>]", "", str)
#print(f"digit: {digit}")

buffer = 5
n_roll = 3
for i in range(n_roll):
    page = browser.get(url)
    tag = page.soup.select("#result")[0]
    digit = tag.text
    print(f"Roll {i+1}: {digit}")

    # don't need to sleep if not rolling dice anymore
    if (i < n_roll - 1):
        print(f"Sleeping for {buffer} seconds...")
        time.sleep(buffer)
