"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    return open(file_path).read()


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()

    for i in range(len(words) - n):
        n_tuple = () # an empty tuple
        for index in range(n):
            n_tuple += (words[i + index], )
        chains[n_tuple] = chains.get(n_tuple, []) + [words[i + n]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    starting_point = choice(list(chains.keys()))
    for word in starting_point:
        words.append(word)
    
    generate_words = True

    while generate_words:
        new_word = choice(chains[starting_point])
        words.append(new_word)
        new_key = ()
        for word in starting_point[1:]:
            new_key += (word,)
        new_key += (new_word, )
            
        if chains.get(new_key, 0) == 0:
            generate_words = False

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)
#print(chains)

# Produce random text
random_text = make_text(chains)

print(random_text)
