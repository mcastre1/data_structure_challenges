def sentence_reversal(sentence):
    """
    Reverse sentence and return a string.
    """
    sentence = sentence.strip()
    
    return " ".join(list(reversed(sentence.split(" "))))


print(sentence_reversal("Hi John, are you ready to go?"))