class Car:
    color=""
    speed=0

    def upspeed(self, value):
        self.speed +=value
        if self.speed >=150:
           self.speed =150 
    
    def downspeed(self, value):
        self.speed -=value

myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0

myCar1.upspeed(180)
print("자동차의 1의 색상은 %s이며,현재속도는 %dkm입니다."%(myCar1.color,myCar1.speed)) 


myCar2.upspeed(60)
print("자동차의 2의 색상은 %s이며,현재속도는 %dkm입니다."%(myCar2.color,myCar2.speed)) 


myCar3.upspeed(0)
print("자동차의 3의 색상은 %s이며,현재속도는 %dkm입니다."%(myCar3.color,myCar3.speed)) 