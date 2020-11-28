def two_fer(name):
    if(type(name) == int):
        raise Exception("name is not a string!")
    if(name.isspace()):
        return "One for you, one for me."
    else:
        return "One for " + name + ", one for me."
