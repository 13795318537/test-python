import yaml


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
        self.hair = hair

    def catch(self):
        print(f'{self.name}抓老鼠')

    def introduce(self):
        print(f'{self.name}是{self.color},{self.age}岁{self.gender}是{self.hair}')


class Dog(Animal):
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def see_home(self):
        print(f'{self.name}看家')

    def bark(self):
        print('汪汪叫')

    def introduce(self):
        print(f'{self.name}是{self.color},{self.age}岁{self.gender}是{self.hair}')


if __name__ == '__main__':
    with open('yaml_demo.yml', encoding="UTF-8") as f:
        dates = yaml.safe_load(f)
        print(dates)

    name = dates['default']['name']
    color = dates['default']['color']
    age = dates['default']['age']
    gender = dates['default']['gender']
    hair = dates['default']['hair']
    if dates['default'] == 'cat':
        cat1 = Cat(name, color, age, gender, hair)
        cat1.catch()
        cat1.introduce()
    else:
        dog1 = Dog(name, color, age, gender, hair)
        dog1.see_home()
        dog1.bark()
        dog1.introduce()

    # Tom = Cat('Tom', 'yollow', 10, '男', 'black')
    # Tom.catch()
    # Tom.introduce()
    # wangcai = Dog('旺财', 'red', 5, '女', 'null')
    # wangcai.see_home()
    # wangcai.bark()
    # wangcai.introduce()
