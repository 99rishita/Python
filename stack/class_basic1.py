class Robots:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduction_self(self):
        print('My name is ' + self.name)
r1 = Robots('Revati', 'blue', 30)
r2 = Robots('Rishita', 'red', 35)
r1.introduction_self()
r2.introduction_self()