class large_cats:
    def __init__(self, name, weight, hunt, place):
        self.name = name
        self.weight = weight
        self.hunt = hunt
        self.place = place

    def introduce(self):
        return f'Hello. My name is {self.name}. I live in {self.place}. My weight is {self.weight}.'

    def hunting(self):
        return f'I live and hunt {self.hunt}'

# tiger = large_cats('Tiger', 300, 'alone', 'Asia')
# print(tiger.introduce())
# print(tiger.hunting())

# lion = large_cats('Lion', 200, 'in pride', 'Africa')
# print(lion.introduce())
# print(lion.hunting())
#
# lepard = large_cats('Lepard', 100, 'alone', 'Africa')
# print(lepard.introduce())
# print(lepard.hunting())

class Cheetah(large_cats):
    def __init__(self, name, weight, hunt, place, speed):
        super().__init__(name,weight,hunt,place)
        self.speed = speed
    def speed(self):
        return f'I can run faster than anyone'
cheetah1 = Cheetah('Cheetah', 100, 'alone', 'Africa', '100 km/h')
print(cheetah1.introduce())
print(cheetah1.hunting())
print(cheetah1.speed())
