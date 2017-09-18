""" This scripts contains several functions and variables that the run.py script calls
Including: 
A function to fetch text from a specfic website - this could be modified to fit the syntax of another website
Text variables of the poems scraped from the website
A function that welcomes the user
A function that prompts the user to select their desired poets and combines the results into an input for the markov chain
"""

import urllib2
from bs4 import BeautifulSoup


######################################################
## Scraping the Sonnets and converting into text files 
######################################################

## A function that takes a URL from the Poetry Foundation website and returns just the text

def getSonnet(url):
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")
	text_nodes = soup.find("div", {"class": "o-poem"}).findAll(text=True) # consult the source html of a website for the appropriate tag to replace "o-poem" with to reproduce the function for another website
	sonnet = '\n'.join(text_nodes)
	return sonnet

## Applying the function to five sonnets to create base options for the user

### Scraping Skakespeare's Sonnet

text_Shakespeare = getSonnet("https://www.poetryfoundation.org/poems/45087/sonnet-18-shall-i-compare-thee-to-a-summers-day")

### Scraping Browning's Sonnet

text_Browning = getSonnet("https://www.poetryfoundation.org/poems/43742/sonnets-from-the-portuguese-43-how-do-i-love-thee-let-me-count-the-ways")

### Scraping Milton's Sonnet

text_Milton = getSonnet("https://www.poetryfoundation.org/poems/44750/sonnet-19-when-i-consider-how-my-light-is-spent")

### Scraping Frost's Sonnet

text_Frost = getSonnet("https://www.poetryfoundation.org/poems/47548/acquainted-with-the-night")

## Scraping Rossetti's Sonnet

text_Rossetti = getSonnet("https://www.poetryfoundation.org/poems/45000/remember-56d224509b7ae")

##############################
## Welcome prompt for the user
###############################

def welcome_prompt():
	print("Welcome to the Markovian Poetry Generator. You will draw inspiration from three famous poets to create your own poem instantly, with math!")

###############################################
## Function to prompt the user for their authors
### Also combines the three selected text into the input for the markov chain
################################################


def markov_input():
	combine_text = ""
	invalidInput = True # creating boolean condition for the while loops
	invalidInput_2 = True
	invalidInput_3 = True
	while(invalidInput): # Checking to make sure the answer is valid
		answer_1 = raw_input("Enter S for Shakespeare, B for Browning, F for Frost, M for Milton, or R for Rossetti: ")
		if answer_1.upper() in ["S", "B", "F", "M", "R"]:
			invalidInput = False
		else:
			print("Enter a valid response")
	if answer_1.upper() == "S": # an if/elif block to select the text
		combine_text = combine_text + text_Shakespeare
	elif answer_1.upper() == "B":
		combine_text = combine_text + text_Browning
	elif answer_1.upper() == "F":
		combine_text = combine_text + text_Frost
	elif answer_1.upper() == "M":
		combine_text = combine_text + text_Milton
	elif answer_1.upper() == "R":
		combine_text = combine_text + text_Rossetti
	while(invalidInput_2): # Checking the answer is valid and not a repeat
		answer_2 = raw_input("Now choose a different poet: S for Shakespeare, B for Browning, F for Frost, M for Milton, or R for Rossetti: ")
		if answer_2.upper() == answer_1.upper():
			print("You have already made that selection")
		elif answer_2.upper() in ["S", "B", "F", "M", "R"]:
			invalidInput_2 = False
		else:
			print("Enter a valid response")
	if answer_2.upper() == "S": # if/elif block to select the text
		combine_text = combine_text + text_Shakespeare
	elif answer_2.upper() == "B":
		combine_text = combine_text + text_Browning
	elif answer_2.upper() == "F":
		combine_text = combine_text + text_Frost
	elif answer_2.upper() == "M":
		combine_text = combine_text + text_Milton
	elif answer_2.upper() == "R":
		combine_text = combine_text + text_Rossetti
	while(invalidInput_3): # Chceking the answer is valid and not a repeat
		answer_3 = raw_input("Make your last selection: S for Shakespeare, B for Browning, F for Frost, M for Milton, or R for Rossetti: ")
		if answer_3.upper() == answer_2.upper() or answer_3.upper() == answer_1.upper():
			print("You have already made that selection")
		elif answer_3.upper() in ["S", "B", "F", "M", "R"]:
			invalidInput_3 = False
		else:
			print("Enter a valid response")
	if answer_3.upper() == "S": # if/elif block selecting the text
		combine_text = combine_text + text_Shakespeare
	elif answer_3.upper() == "B":
		combine_text = combine_text + text_Browning
	elif answer_3.upper() == "F":
		combine_text = combine_text + text_Frost
	elif answer_3.upper() == "M":
		combine_text = combine_text + text_Milton
	elif answer_3.upper() == "R":
		combine_text = combine_text + text_Rossetti 
	return combine_text
