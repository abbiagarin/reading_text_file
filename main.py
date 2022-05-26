# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


from dataclasses import replace
import string


def read_file_content(filename):
    with open(filename) as file:
        contents = file.read()
        return contents


def count_words():
    text = read_file_content("./story.txt")

    counts = dict()
    for character in string.punctuation:
        text = text.replace(character, "")
        words = text.split()
        # print(words)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(read_file_content("story.txt"))
print('Find the number of occurrence in text file below: \n', count_words())
