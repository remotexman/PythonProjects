class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.owner = owner

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i.lower():
                self.__color = new_color
        if self.__color != new_color:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

if __name__ == '__main__':
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

    vehicle1.print_info()

    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    vehicle1.print_info()