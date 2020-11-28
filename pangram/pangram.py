def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters_used = []
    sentence = sentence.lower()
    for x in sentence:
        if(x in alphabet):
            if(x == " "):
                continue
            elif(not(x in letters_used)):
                letters_used.append(x)

    if(len(letters_used) == 26):
        return True
    else:
        return False