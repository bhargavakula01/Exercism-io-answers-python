def abbreviate(words):
    list_words = words.split(' ')

    for x in range(len(list_words)):
        newStr = ''
        for y in range(len(list_words[x])):
            if(list_words[x][y].isalpha() or list_words[x][y] == "-"):
                newStr += list_words[x][y]
        list_words[x] = newStr


    acronym_str = ''
    for x in list_words:
        if(x[0].isalpha()):
            acronym_str += x[0]
        if(x.find('-') >= 0):
            index = x.find("-")
            if(index != len(x)-1):
                acronym_str += x[index+1]
    
    return acronym_str.upper()