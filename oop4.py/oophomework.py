class Car:  
    speed=0
    def upspeed(self,value):
        self.speed += value

        print("현재 속도(슈퍼클래스):%d"%self.speed)

class sedan(Car):   
    def upspeed(self,value):
        self.speed+=value

        if self.speed>150:
            self.speed=150
        print("현재 속도(서브클래스):%d"%self.speed)
class sonata(sedan):
    pass    
class Truck(Car):
    pass
sedan1, truck1, sonata1= None, None, None

truck1=Truck()
sedan1=sedan()
sonata1=sonata()

print("트럭->", end="") 
truck1.upspeed(200)

print("승용차->",end="")    
sedan1.upspeed(200)

print("소나타->",end="")    
sonata1.upspeed(200)    