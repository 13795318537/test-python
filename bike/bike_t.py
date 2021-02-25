import yaml


class Bike:
    def run(self, km):
        print(f'自行车骑行{km}')


class E_Bike(Bike):
    def __init__(self, dianliang):
        self.dianliang = dianliang

    def vol(self, vol):
        self.dianliang = self.dianliang + vol

    def run(self, km):
        miles = km - self.dianliang * 10
        if miles > 0:
            print(f'电动开了{self.dianliang * 10}')
            super().run(miles)
        else:
            print(f'电动开了{km}')


if __name__ == '__main__':
    with open("demoyaml.yml") as f:
        dates = yaml.safe_load(f)

        print(dates["E1"])
        dianliang = dates["dafaul"]["dianliang"]
        km = dates["dafaul"]["run_km"]
        b = E_Bike(dianliang)
        b.run(km)

    # a = Bike()
    # a.run(111)
    # b = E_Bike(10)
    # # b.vol(5)
    # b.run(102)
