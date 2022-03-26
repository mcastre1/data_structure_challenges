def word_split(phrase, list_of_words, output = None):
    '''
    Recursevily splits the given phrase into words found in the list of words.
    '''
    # If this is the first time through, then set output to an empty list.
    if output == None:
        output = []

    # Iterate through each word in the list of words,
    # and check whether the remaining phrase starts with the word
    # If so, then keep track of it by appending it to the output list
    # and call the word_split function recursevily with the remainding piece
    # of the phrase.
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):], list_of_words, output)

    # Finally, if the remaining of the phrase doesnt exist in the list of words,
    # we return the output list.
    return output


print(word_split("themanran", ['the', 'ran', 'man']))