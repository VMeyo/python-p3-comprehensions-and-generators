# 1. Fucntion that returns a list of all the even numbers.

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0] # Use quotient to check on the remainder so as to check even numbers
    
# 2. Function that returns a list of sentence strings with exclamation marks
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list] # Concatenate the 1st portion of sentence with an '!'


    