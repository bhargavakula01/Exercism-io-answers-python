class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        index = 0
        if(len(self.card_num) <= 1 or self.card_num[0] == ' '):
            return False
        numbers_store = []
        for x in range(len(self.card_num)):
            if(self.card_num[x] != " " and (not self.card_num[x].isnumeric())):
                return False
            elif(self.card_num[x] != ' '):
                numbers_store.append(int(self.card_num[x]))
        for z in range(len(numbers_store)-1, -1, -1):
            if(index % 2 == 1):
                temp_num = numbers_store[z] * 2
                if(temp_num > 9):
                    temp_num -= 9
                    numbers_store[z] = temp_num
                else:
                    numbers_store[z] = temp_num
            index+=1
        total = 0
        for y in numbers_store:
            total += y
        if(total % 10 == 0):
            return True
        else:
            return False
