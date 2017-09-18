"""" This file ties the flow of the application together.
It should be run from the terminal.
The program will ask a user to choose 3 out of 5 poets to use to generate a poem 
whose length they can choose """

import fetch_data # The other script created for this program
from Markov_Chain.cc_markov import MarkovChain # the provided markov chain to branch


fetch_data.welcome_prompt() # welcoming the user

input_data = fetch_data.markov_input() # prompting the user to select the poets

mc = MarkovChain() # imitalizing the markov chain

mc.add_string(input_data) # providing the user generated input

n_words = int(raw_input("How many words do you want the poem to be? "))

print "Your %s word poem  is: "%n_words

poem = mc.generate_text(n_words) # generating the markov chain output
poem_join = " ".join(poem) # joining the words into one string
poem_clean = poem_join[0].upper() + poem_join[1: ] # capitalizing the first letter


print(poem_clean) # Displaying the final poem
