def count_words(sentence):
    sentence = sentence.lower()
    newSentence = sentence_reform(sentence)

    list_sentence = newSentence.split(' ')
    list2 = []
    for x in list_sentence:
        if(not len(x) == 0):
            list2.append(x)

    list2 = remove_symbols(list2)
    print(list2)
    list2 = remove_extra_quotes(list2)
    print(list2)
    sentence_dictionary = dict()
    for x in list2:
       sentence_dictionary[x] = 0
    
    for x in list2:
       sentence_dictionary[x] += 1

    return sentence_dictionary 


def sentence_reform(sentence):
    newSentence = ""
    for x in sentence:
        if(not(x == ',' or x == '\n' or x == '\t' or x == ':' or x == '.' or x == "_")):
            newSentence += x
        if(x == '\n' or x == '\t' or x =="  " or x == "_" or x == ","):
            newSentence += " "
    return newSentence


def remove_symbols(list_sentence):
    for x in range(len(list_sentence)):
        newSentence = ''
        for y in range(len(list_sentence[x])):
            if(list_sentence[x][y].isalpha() or list_sentence[x][y] == "'" or list_sentence[x][y].isdigit()):
                newSentence += list_sentence[x][y]
        list_sentence[x] = newSentence
    return list_sentence

def remove_extra_quotes(list_sentence):
    for x in range(len(list_sentence)):
        newSentence = ''
        if(len(list_sentence[x]) > 1):
            if(list_sentence[x][0] == "'" and list_sentence[x][1] == "'" and list_sentence[x][len(list_sentence[x])-1] == "'" and list_sentence[x][len(list_sentence[x])-2] == "'"):
                for y in range(2,len(list_sentence[x])-2):
                    newSentence += list_sentence[x][y]
                list_sentence[x] = newSentence
            elif(list_sentence[x][0] == "'" and list_sentence[x][len(list_sentence[x])-1] == "'"):
                for y in range(1,len(list_sentence[x])-1):
                    newSentence += list_sentence[x][y]
                list_sentence[x] = newSentence
    return list_sentence

