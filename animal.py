class Animal():
    def __init__(self, name, speak):
        self.name = name
        self.speak = speak
        print(f"동물 {name}은 {speak}!")

class Dog(Animal):
    def __init__(self, name, speak):
        super().__init__(name, speak)

class Cat(Animal):
    def __init__(self, name, speak):
        super().__init__(name, speak)


dog = Dog("비숑", "멍멍")
cat = Cat("코숏", "야옹")

dog
cat