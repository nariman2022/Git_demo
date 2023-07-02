class Dog:

    def __init__(self, name, sex, height, weight):
        self.name = name
        self.sex = sex
        self.height = height
        self.weight = weight

    def run(self):
        return 'I can run'

    def get_name(self):
        return f'Hello, my name is {self.name}'


class Pitbull(Dog):

    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)
