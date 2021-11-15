from classes import sportwear


class TrackSuit(sportwear.SportWear):

    def __init__(
        self, suit_size: str,
        persantage_of_cotton: int,
        price: float, brand, color, sex
    ):
        super().__init__(price, color, brand, sex)
        self.__suit_size = suit_size
        self.__persantage_of_cotton = persantage_of_cotton

    def __str__(self):
        return f'suit_size = {self.__suit_size} \n' \
               f'persantage_of_cotton = {self.__persantage_of_cotton} \n' \
               f'price = {self._price} \n' \
               f'brand =  {self._brand} \n'\
               f'color = {self._color} \n' \
               f'sex = {self._sex} \n'



    def get_suit_size(self):
        return self.__suit_size

    def get_persantage_of_cotton(self):
        return self.__persantage_of_cotton

    def set_suit_size(self,suit_size):
        self.__suit_size = suit_size

    def set_persantage_of_cotton(self,persantage_of_cotton):
       self.__persantage_of_cotton = persantage_of_cotton