"""
Write a program to count the occurrences of words in a string. The program should ask the user for a string, then print the counts of how many of each word are in the string.
The output should look like this (depending on user input):

Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2


Word Occurrences
Estimate: 20 minutes
Actual:   16 minutes

"""


text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

words = list(word_to_count.keys())
words.sort()
len_longest_word = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, len_longest_word, word_to_count[word]))
