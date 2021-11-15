from classes import sportwear


class SportShoes(sportwear.SportWear):

    def __init__(self, shoes_size: float, price, brand, color, sex):
        super().__init__(price, color, brand, sex)
        self.__shoes_size = shoes_size

    def __str__(self):
        return f'shoes_size = {self.__shoes_size} \n' \
               f'price = {self._price} \n' \
               f'brand =  {self._brand} \n'\
               f'color = {self._color} \n' \
               f'sex = {self._sex} \n'

    def get_shoes_size(self):
        return self.__shoes_size

    def set_shoes_size(self, shoes_size):
        self.__shoes_size = shoes_size
