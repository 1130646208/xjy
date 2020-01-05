import time as t

class MyTimer():
    def __init__(self):
        self.unit=['year','month','day','hour','min','sec']
        self.prompt = 'not begin!'
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __add__(self,other):
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
        if result[index]:
            prompt = 'all run time sum is :' + str(result[index]) + self.unit[index]
            print(prompt)



        
        
    #start
    def start(self):
        self.begin = t.localtime()
        self.prompt = 'please stop()!'
        print('start timing...')

    #stop
    def stop(self):
        if not self.begin:
            print ('please start()!')
        else:
            self.end = t.localtime()
            self._calc()
            print('end timing...')


    #calculate time  internal method
    def _calc(self):
        self.lasted = []
        self.prompt = 'run last for:'
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]
            
        print(self.prompt)
        self.begin = 0
        self.end = 0
        
