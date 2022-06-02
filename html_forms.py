# Description: Interact with HTML forms via MechanicalSoup
# Author: Haley Hunter-Zinck
# Date: 2022-06-01
# Tutorial: https://realpython.com/python-web-scraping-practical-introduction/
# Installation: python3 -m pip install MechanicalSoup
# Install details: python3 -m pip show mechanicalsoup

import mechanicalsoup

url = "http://olympus.realpython.org/login"

#############################
#   mechanical soup browser #
#############################

browser = mechanicalsoup.Browser()
page = browser.get(url)
print(page) # 200 = successful

print(f"page type: {type(page.soup)}")
print(f"page html: {page.soup}")

##############################
#   fill out the login form  #
##############################

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

# 4
print(profiles_page.url)


#################################
#   extract info after login    #
#################################

base_url = "http://olympus.realpython.org"

links = profiles_page.soup.select("a")
for link in links:
    print(f"{link.text}: {base_url + link['href']}")

#################
#   exercise    #
#################

title = profiles_page.soup.title
print(title)
