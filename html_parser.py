# Description: HTML parser tool 
# Author: Haley Hunter-Zinck
# Date: 2022-06-01
# install: python3 -m pip install beautifulsoup4
# show install details: python3 -m pip show beautifulsoup4

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

url_dionysus = "http://olympus.realpython.org/profiles/dionysus"

#################
#   soup object #
#################

html = urlopen(url_dionysus).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print("--- raw HTML ---")
print(html)
print("--- raw text via bs4 ---")
print(soup.get_text())
print("--- cleaned text via bs4 ---")
print(re.sub("\n+", "\n", soup.get_text()))
print("--- get all tags via bs4 ---")


#########################
#   find tags via bs4   #
#########################

print(soup.find_all("img"))

image1, image2 = soup.find_all("img")
print(f"image1.name = '{image1.name}'")
print(f"image1 src: {image1['src']}")
print(f"image2 src: {image2['src']}")

print(f"cleaned title tag: '{soup.title}'")

print(f'specific image tag: {soup.find_all("img", src="/static/dionysus.jpg")}')


#####################
#      exercise     #
#####################

# description: Using Beautiful Soup, print out a list of all the 
# links on the page by looking for HTML tags with the name a and 
# retrieving the value taken on by the href attribute of each tag.

url_profile = "http://olympus.realpython.org/profiles"
base_url = "http://olympus.realpython.org"

html = urlopen(url_profile).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(html)

tag_a = soup.find_all("a")
print(tag_a)

for tag in tag_a:
    print(base_url + tag["href"])
