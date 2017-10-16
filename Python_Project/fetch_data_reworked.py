import urllib2
from bs4 import BeautifulSoup
from time import sleep

##############################
## Welcome prompt for the user
###############################

def welcome_prompt():
	print("Welcome to the Markovian Poetry Generator. You will draw inspiration from three famous poets to create your own poem instantly, with math!")


## Dictionary of input URLs
poet_dic = {'S': "https://www.poetryfoundation.org/poems/45087/sonnet-18-shall-i-compare-thee-to-a-summers-day",
'B': "https://www.poetryfoundation.org/poems/43742/sonnets-from-the-portuguese-43-how-do-i-love-thee-let-me-count-the-ways",
'M': "https://www.poetryfoundation.org/poems/44750/sonnet-19-when-i-consider-how-my-light-is-spent",
'F': "https://www.poetryfoundation.org/poems/47548/acquainted-with-the-night",
'R': "https://www.poetryfoundation.org/poems/45000/remember-56d224509b7ae"}


def getSonnet(url):
	"""Function to retrieve the poem in text form """
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "lxml")
	text_nodes = soup.find("div", {"class": "o-poem"}).findAll(text=True) # consult the source html of a website for the appropriate tag to replace "o-poem" with to reproduce the function for another website
	sonnet = '\n'.join(text_nodes)
	return sonnet

def UserInput():
	"""Function that prompts the user to select 2-5 poets"""
        input_vector = []
        invalidInput = True
        invalidInput2 = True
        num_poets = 0
        while(invalidInput):
                num_poets = int(raw_input('How many poets would you like to combine? Please select 2-5:'))
                if num_poets in [2, 3, 4, 5]:
                        invalidInput = False
                else:
                        print('Enter a valid response')
        for i in range(0, num_poets):
                invalidInput2 = True
                while(invalidInput2):
                        user_input = raw_input("Enter S for Shakespeare, B for Browning, F for Frost, M for Milton, or R for Rossetti: ")
                        if user_input.upper() in poet_dic.keys():
                                invalidInput2 = False
                                input_vector.append(user_input.upper())
                        else:
                                print("Please enter a valid response.")
        return input_vector

def MarkovInput(input_list):
	"""Generates input for the code academy markov chain """
	combine_text = ""
	for entry in input_list:
		combine_text = combine_text + getSonnet(poet_dic[entry])
	return combine_text

def PoemGen(input_list):
	"""Creates a poem by combining parts of the original poems"""
	combine_text = ""
	for entry in input_list:
		text = getSonnet(poet_dic[entry])
		combine_text = combine_text + text[ :(len(text)/ len(input_list))]
	return combine_text