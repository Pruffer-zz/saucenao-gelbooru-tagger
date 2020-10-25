# Import libs

from saucenao_api import SauceNao
from bs4 import BeautifulSoup
import requests

# Get image from Gelbooru DB & search

results = SauceNao(db=25).from_url('IMAGE URL HERE')

# Assign the variable 'best' the first result's URL & print

best = ''.join(results[0].urls)
print('URL Found: ' + best)

# Get page

html = requests.get(best).text

# Parse tags' parent <li> elements from page

soup = BeautifulSoup(html, "lxml")
list = soup.find_all("li", attrs={"class": "tag-type-general"})

# Define empty tag list

tags = []

# Add tags to list, ignore '?' link

# For each <li>
for item in list:
	# Find all <a> elements
	for a in item.find_all("a"):
		# If <a> element's content isn't '?'
		if ''.join(a.contents) != '?':
			# Add it to the list
			tags.append(''.join(a.contents))

# Print

print(tags)
