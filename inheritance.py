# inheritance
class Animal:
    def __init__(self):
        self.color = ""
        self.eat = ""
    
    def set_color (self,color):
        self.color = color

    def set_eat (self,eat):
        self.eat = eat

class Dog(Animal):
    def __init__(self):
        self.name = ""
        self.sound = ""

    def set_name (self,name) :
        self.name = name

    def set_sound(self, sound):
        self.sound = sound

    def __str__(self):
        return f"name = {self.name} color = {self.color} eat = {self.eat} sound = {self.sound}"

class Cat(Dog):
     def __str__(self):
        return f"name = {self.name} color = {self.color} eat = {self.eat} sound = {self.sound}"
    
dog = Dog() 
dog.set_name("VAVA")
dog.set_color("red") 
dog.set_eat("snack")
dog.set_sound("boo")

cat = Cat()
cat.set_name("Hello")
cat.set_sound("meow")
cat.set_color("blue")
cat.set_eat("tuna")

print(dog)
print(cat)