def print_upper_words(words):

    '''prints words in uppercase, 
    the print() function puts them on seperate lines
    '''
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    '''same as previous function except it only 
    prints the word if the word starts with e or E '''
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    '''prints word if it contains the letters in the must_start_with array'''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


