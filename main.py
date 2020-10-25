# Import libs
from saucenao_api import SauceNao
from bs4 import BeautifulSoup
import requests
import json

# Get image from Gelbooru DB & search
results = SauceNao(db=25).from_url('INSERT URL HERE')

# Assign the variable 'best' the first result's URL & print
best = ''.join(results[0].urls)
print('URL Found: ' + best)

# Get page
html = requests.get(best).text

# Parse tags' parent elements from page
soup = BeautifulSoup(html, "lxml")

# Make list of tag types & prepare empty tag dictionary
types = ['general', 'character', 'artist', 'copyright', 'metadata']
result = dict.fromkeys(types, [])

# For every type of tag..
for item in types: 
	# Find all <li> elements of tag type
	list = soup.find_all("li", attrs={"class": "tag-type-" + item})

	# Make empty tag list
	tags = []

	# For each tag parent element..
	for tag in list:
		# Find all <a> elements
		for a in tag.find_all("a"):
			# If <a> element's content isn't '?', then..
			if ''.join(a.contents) != '?':
				# Add it to the list
				tags.append(''.join(a.contents))

	# Put list into dictionary
	result[item] = tags

# JSON-ify and print
json = json.dumps(result, indent=4)
print(json)
