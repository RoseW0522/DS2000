''' Ruisi Wang
    DS2000
    Homework 8 (the resubmission of Homework 6)
    April 17, 2022
    wheel.py
'''

import random

vowel = ["A", "E", "I", "O", "U"]
pre = ["R", "S", "T", "L", "N", "E"]

filename = "puzz.txt"

def read_file(filename):
    ''' Function: read_file
        Parameter: one string
        Returns: list of strings, one per line in the file
    '''
    phrases = []
    with open(filename, "r") as infile:
        while True:
            phrase = infile.readline().strip()
            if phrase == "":
                break
            phrases.append(phrase)
    return phrases

def clean_string(input_st):
    ''' Function: clean_string
        Parameter: one string
        Returns: new version of the string, cleaned up
    '''
    output_st = ""
    for letter in input_st:
        if letter.isalpha():
            output_st += letter.upper()
        else:
            output_st += letter
    return output_st

def count_letters(d, letter):
    ''' Function: count_letters
        Parameter: one dictionary and one string
        Returns: count the number of appearing in the phrases
    '''
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1

def partial_phrase(phrase):
    ''' Function: partial_phrase
        Parameter: one string
        Returns: present the letter only if they are the common five letters,
         and show the top 3 appear-in-phrase letters except those five letters
    '''
    partial = ""
    for i in phrase:
        if i in pre:
            partial += i
        else:
            partial += " "
    return partial

def main():
    # read the file and make a list of phrases
    phrases = read_file(filename)
    # random choose a phrase in the list of phrases
    phrase = random.choice(phrases)
    # clean the phrase without the punctuation and space
    clean = clean_string(phrase)
    
    # clean all the phrases in the list and make a new list
    cleans = []
    for phrase in phrases:
        cleans.append(clean_string(phrase))
    
    # find the times of each vowel and consonant appearing in the phrases
    vowel_num = {}
    consonant_num = {}
    for clean_phrase in cleans:
        for cleaned in clean_phrase:
            if cleaned in vowel and cleaned not in pre:
                count_letters(vowel_num, cleaned)
            if cleaned not in vowel and cleaned not in pre and cleaned!=" ":
                count_letters(consonant_num, cleaned)
    
    # sort the order of vowel and consonant into the appearance time
    # from the most to the least
    vowel_sorted = sorted(vowel_num.items(), 
                          key = lambda x:x[1], reverse = True)
    consonant_sorted = sorted(consonant_num.items(), 
                              key = lambda x:x[1], reverse = True)
    # show the clean partial phrase with only the allowed letters
    print(partial_phrase(clean))
    
    # show the top three in the consonants set 
    # add them into the allowed letter set
    print("The most common consonants are:", consonant_sorted[0][0], 
          consonant_sorted[1][0], consonant_sorted[2][0])
    pre.append(consonant_sorted[0][0])
    pre.append(consonant_sorted[1][0])
    pre.append(consonant_sorted[2][0])
    
    # show the top one in the vowel set 
    # add them into the allowed letter set
    print("The most common vowel is:", vowel_sorted[0][0])
    pre.append(vowel_sorted[0][0])
    
    # show the clean partial phrase
    print(partial_phrase(clean))
    
    
    guess = input("Enter the guess, including spaces and punctuation.\n")
    if clean_string(guess) == clean:
        print("Correct!")
    else:
        print("Sorry loser, you lost :(\n",
              "The puzzle was:", clean)
    
main()

















