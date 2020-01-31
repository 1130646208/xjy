class CelDeg:
    
    def __init__(self, val=26.0):
        self.val = val
        
    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        self.val = value
    

class FahDeg:
    
    def __get__(self, instance, owner):
        return instance.cel* 1.8 + 32
    
    def __set__(self, instance, value):
        instance.cel = (value - 32) / 1.8


class Temprature:
    fah = FahDeg()
    cel = CelDeg()
