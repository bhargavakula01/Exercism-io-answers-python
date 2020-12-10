class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        self.format()
        if(self.hour < 10 or self.minute < 10):
            if(self.hour < 10 and not self.minute < 10):
                return "0" + str(self.hour) + ":" + str(self.minute)
            elif(not self.hour < 10 and self.minute < 10):
                return str(self.hour) + ":" + "0" + str(self.minute)
            else:
                return "0" + str(self.hour) + ":" + "0" + str(self.minute)
        else:
            return str(self.hour) + ":" + str(self.minute)
        
    def __eq__(self, other):
        self.format()
        other.format()
        if(self.hour == other.hour):
            if(self.minute == other.minute):
                return True
            else:
                return False
        else:
            return False
        

    def __add__(self, minutes):
        self.minute += minutes
        self.format()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.format()
        return self

    def format(self):
        if(self.minute >= 60):
            count = 0
            while(self.minute >= 60):
                count+=1
                self.minute -= 60
            self.hour += count
        elif(self.minute < 0):
            count = 0
            while(self.minute < 0):
                count += 1
                self.minute += 60
            self.hour -= count
        
        if(self.hour >= 24):
            while(self.hour >= 24):
                self.hour-= 24
        elif(self.hour < 0):
            while(self.hour < 0):
                self.hour += 24

