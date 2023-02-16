import enchant

def check_spelling(word):
    
    d = enchant.Dict("en_US")

    
    if d.check(word):
        print("The word", word, "is spelled correctly.")
    else:

        suggestions = d.suggest(word)
        print("The word", word, "is misspelled, Did you mean:")
        for suggestion in suggestions:
            print(suggestion)

#write the word in 'check_spelling()' function.
check_spelling(" ")
check_spelling(" ")