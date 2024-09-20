class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, __model):
        self.__model = __model
        print(f"Модель: {self.__model}")
        return

    def get_horsepower(self, __engine_power):
        print(f"Мощность двигателя: {self.__engine_power}")
        return

    def get_color(self, __color):
        print(f"Цвет: {self.__color}")
        return

    def print_info(self):
        self.get_model(self.__model)
        self.get_horsepower(self.__engine_power)
        self.get_color(self.__color)
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color

        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()