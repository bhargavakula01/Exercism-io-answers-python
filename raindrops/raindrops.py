def convert(number):
    int_num = int(number)
    solution = ""
    if(int_num % 3 == 0):
        solution += 'Pling'
    if(int_num % 5 == 0):
        solution += 'Plang'
    if(int_num % 7 == 0):
        solution += 'Plong'
    if(not(int_num % 7 == 0 or int_num % 5 == 0 or int_num % 3 == 0)):
        return str(number)
    return solution