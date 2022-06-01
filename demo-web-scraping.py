# Description: 
# Author: Haley Hunter-Zinck
# Date: 2022-
# tutorial: https://realpython.com/python-web-scraping-practical-introduction/

from urllib.request import urlopen

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