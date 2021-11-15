class SportWear:

    def __init__(self, price: float, color, brand, sex):
        self._price = price
        self._color = color
        self._brand = brand
        self._sex = sex

    def __str__(self):
        return f'price = {self._price} \n' \
        f'color = {self._color} \n' \
        f'brand = {self._brand} \n' \
        f'sex=  {self._sex} \n'



    def get_price(self):
        return self._price

    def get_color(self):
        return self._color

    def get_brand(self):
        return self._brand

    def get_sex(self):
        return self._sex

    def set_price(self, price):
        self._price = price

    def set_color(self,color):
        self._color = color

    def set_brand(self, brand):
        self._brand = brand

    def set_sex(self, sex):
        self._sex = sex


if __name__ == '__main__':
    pass