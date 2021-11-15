from classes import enums


class SportWearManager:

    def __init__(self, sportwear_list):
        self.__sportwear_list = sportwear_list

    def __str__(self):
        return f'shoes_size = {self.__shoes_size} \n' \
               f'price = {self._price} \n' \
               f'brand =  {self._brand} \n' \
               f'color = {self._color} \n' \
               f'sex = {self._sex} \n' \


    def get_sportwear_list(self):
        return self.__sportwear_list

    def set_sportwear_list(self,sportwear_list):
        self.__sportwear_list = sportwear_list

    def add_sportwear(self,sportwear):
        self.__sportwear_list.append(sportwear)
        return  self.__sportwear_list




    def search_by_brand(self, brand):
        searched_brand = []
        for items in self.__sportwear_list:
            if items.get_brand() == brand:
                searched_brand.append(items)
        return searched_brand

    def sort_by_price(self, order):
        if order == enums.SortType.ASC:
            self.__sportwear_list.sort(key=lambda c: c.get_price())

        if order == enums.SortType.DESC:
            self.__sportwear_list.sort(key=lambda c: c.get_price(), reverse=True)
        return self.__sportwear_list



