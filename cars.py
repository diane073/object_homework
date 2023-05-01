class Car():
    def __init__(self, model, color, speed=0):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        accel = 20 
        self.speed += accel
        print(f"{self.model} accelerate!")

    
    def brake(self):
        brk = 10
        self.speed -= brk
        print(f"{self.model} brake!")

        
    def get_speed(self):
        print(f"{self.model}의 현재 속도는 {self.speed}km/h입니다.")


car = Car("소나타", "자주색",0)

car.accelerate()
car.brake()
car.brake()
car.get_speed()
