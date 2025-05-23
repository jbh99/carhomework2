class Car:
    name=""
    speed=0
    
    def __init__(self,name,speed):
         self.name=name
         self.speed=speed


    def getName(self):
        return self.name

    def getspeed(self):
        return self.speed

Car1,Car2=None,None    

Car1=Car("아우디",0)
Car2=Car("벤츠",30)

print(" %s의현재속도는 %dkm입니다."%(Car1.getName(),Car1.getspeed())) 
print(" %s의현재속도는 %dkm입니다."%(Car2.getName(),Car2.getspeed())) 

 