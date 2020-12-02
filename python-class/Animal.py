class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def run(self):
        print(f'running')

    def bark(self):
        print('barking')


class Cat(Animal):
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = '短毛'

    def catch(self):
        print(f'{self.name}抓老鼠')

    def introduce(self):
        print(f'{self.name}是{self.color},{self.age}岁{self.gender}是{self.hair}')


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = '长毛'

    def see_home(self):
        print(f'{self.name}看家')

    def bark(self):
        print('汪汪叫')

    def introduce(self):
        print(f'{self.name}是{self.color},{self.age}岁{self.gender}是{self.hair}')


if __name__ == '__main__':
    Tom = Cat('Tom', 'yollow', 10, '男', 'black')
    Tom.catch()
    Tom.introduce()
    wangcai = Dog('旺财', 'red', 5, '女', 'null')
    wangcai.see_home()
    wangcai.bark()
    wangcai.introduce()
