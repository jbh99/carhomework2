class Car:
    color=""
    speed=0
    count=0

    def __init__(self):
         self.speed=0
         Car.count+=1

myCar1,myCar2=None,None    

myCar1=Car()
myCar1.speed=30
print(" 자동차1의 현재속도는 %dkm입니다, 생산된 자동차는 %d입니다."%(myCar1.speed,Car.count)) 

myCar2=Car()
myCar2.speed=60
print(" 자동차1의 현재속도는 %dkm입니다, 생산된 자동차는 %d입니다."%(myCar2.speed,myCar2.count)) 
