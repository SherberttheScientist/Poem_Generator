"""" This file ties the flow of the application together.
It should be run from the terminal.
The program will ask a user to 2 to 5 poets to use to generate a poem 
by MarkovChain, whose length they can choose.
Additionally, a poem is created by combining parts of the works of the 
selected authors.  """

import fetch_data_reworked # The other script created for this program
from Markov_Chain.cc_markov import MarkovChain # the provided markov chain to branch

fetch_data_reworked.welcome_prompt() # welcoming the user

user_input = fetch_data_reworked.UserInput() # getting the input from the user

markov_input = fetch_data_reworked.MarkovInput(user_input) # generating the input for the Markov chain

mc = MarkovChain() # initalizing  an object in the the markov chain class

mc.add_string(markov_input) # providing the user generated input

n_words = int(raw_input("How many words do you want the poem to be? "))

print "Your %s word poem  is: "%n_words

poem = mc.generate_text(n_words) # generating the markov chain output
poem_join = " ".join(poem) # joining the words into one string
poem_clean = poem_join[0].upper() + poem_join[1: ] # capitalizing the first letter


print(poem_clean) # Displaying the final poem

print('Hmmm... Statistical crafted, but meaningless. How about some light plagerism instead? ')

poem_combo = fetch_data_reworked.PoemGen(user_input)

print(poem_combo)