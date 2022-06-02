# Description: String parsing of HTML with regex.
# Author: Haley Hunter-Zinck
# Date: 2022-06-01
# Tutorial: https://realpython.com/python-web-scraping-practical-introduction/

from urllib.request import urlopen
import re

# paramters
url_aphrodite = "http://olympus.realpython.org/profiles/aphrodite"
url_poseidon = "http://olympus.realpython.org/profiles/poseidon"
url_dionysus = "http://olympus.realpython.org/profiles/dionysus"

#########################
#       aphrodite       #
#########################

# link to page
page = urlopen(url_aphrodite)

# read full text on a page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# find conntens associated with a specific tag
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(f"title: '{title}'")

#########################
#       poseidon       #
#########################

page = urlopen(url_poseidon)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# find title with previous approach
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(f"title take 1: '{title}'")

# find title with approach accounting for html typo
title_index = html.find("<title >")
start_index = title_index + len("<title >")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(f"title take 2: '{title}'")

######################
#       regex        #
######################

# asterisk (*) behavior: zero or more of previous character
print(f"regex 01: {re.findall('ab*c', 'ac')}")
print(f'regex 01: {re.findall("ab*c", "abcd")}')
print(re.findall("ab*c", "acc"))
print(re.findall("ab*c", "abcac"))
print(re.findall("ab*c", "abdc"))
print(re.findall("ab*c", "ABC"))
print(re.findall("ab*c", "ABC", re.IGNORECASE))

# period (.) behavior: any single character
print(re.findall("a.c", "abc"))
print(re.findall("a.c", "abbc"))
print(re.findall("a.c", "ac"))
print(re.findall("a.c", "acc"))

# combos of period and asterisk
print(re.findall("a.*c", "abc"))
print(re.findall("a.*c", "abbc"))
print(re.findall("a.*c", "ac"))
print(re.findall("a.*c", "acc"))

# search function
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
print(f"'ab*c' in 'ABC' ignoring case: '{match_results.group()}'")

# sub function and question mark (?)
string = "Everything is <replaced> if it's in <tags>."
print(f"original string: {string}")
greedy = re.sub("<.*>", "ELEPHANTS", string)
print(f"greedy sub: {greedy}")
minsub = re.sub("<.*?>", "ELEPHANTS", string)
print(f"greedy sub: {minsub}")

#################
#   dionysus    #
#################

page = urlopen(url_dionysus)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# <TITLE >Profile: Dionysus</title  / >

pattern = "<title.*?>.*?</title.*?>"
title_plus = re.search(pattern, html, re.IGNORECASE).group()
title = re.sub("<.*?>", "", title_plus, re.IGNORECASE)
print(title)

#################
#   exercise 1  #
#################

# description use .find() to display the text following “Name:” and “Favorite Color:” 
# (not including any leading spaces or trailing HTML tags that might appear on the 
# same line).

# read html
page = urlopen(url_dionysus)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# get name text
for search_str in ["Name: ", "Favorite Color: "]:
    name_index = html.find(search_str)
    start_index = name_index + len(search_str)
    end_index = start_index + html[start_index:].find("<")
    str_raw = html[start_index:end_index]
    str_clean = re.sub("[ \n\t\r*]", "", str_raw)
    print(f"{search_str}'{str_clean}'")
