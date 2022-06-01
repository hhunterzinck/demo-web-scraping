# Description: 
# Author: Haley Hunter-Zinck
# Date: 2022-06-01
# tutorial: https://realpython.com/python-web-scraping-practical-introduction/

from urllib.request import urlopen

import re

# paramters
url_aphrodite = "http://olympus.realpython.org/profiles/aphrodite"
url_poseidon = "http://olympus.realpython.org/profiles/poseidon"

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
re.findall("ab*c", "ac")
re.findall("ab*c", "abcd")
re.findall("ab*c", "acc")
re.findall("ab*c", "abcac")
re.findall("ab*c", "abdc")
re.findall("ab*c", "ABC")
re.findall("ab*c", "ABC", re.IGNORECASE)

# period (.) behavior: any single character
re.findall("a.c", "abc")
re.findall("a.c", "abbc")
re.findall("a.c", "ac")
re.findall("a.c", "acc")

# combos of period and asterisk
re.findall("a.*c", "abc")
re.findall("a.*c", "abbc")
re.findall("a.*c", "ac")
re.findall("a.*c", "acc")

# search function
match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group()
