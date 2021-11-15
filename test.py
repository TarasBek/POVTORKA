import unittest
import classes
from classes import enums, sportshoes, sportwearmanager, track_suit, sportwear
from classes import sportwearmanager


class TestUnderWearManager(unittest.TestCase):

    def setUp(self):
        self.first_sportshoes = classes.sportshoes.SportShoes(
            42, 1500, classes.enums.Brand.NIKE, classes.enums.Color.BLUE, classes.enums.Sex.UNISEX)
        self.second_sportshoes = classes.sportshoes.SportShoes(
            38, 2000, classes.enums.Brand.ADIDAS, classes.enums.Color.RED, classes.enums.Sex.MALE)

        self.first_tracksuit = classes.track_suit.TrackSuit(
            42, 100, 3000, classes.enums.Brand.PUMA, classes.enums.Color.WHITE, classes.enums.Sex.FEMALE)
        self.second_tracksuit = classes.track_suit.TrackSuit(
            38, 70, 3500, classes.enums.Brand.ASICS, classes.enums.Color.PURPLE, classes.enums.Sex.MALE)
        self.third_tracksuit = classes.track_suit.TrackSuit(
            38, 70, 3500, classes.enums.Brand.ASICS, classes.enums.Color.PURPLE, classes.enums.Sex.MALE)

        sportwear_list = [self.first_sportshoes, self.second_sportshoes, self.first_tracksuit, self.second_tracksuit]
        self.brand = enums.Brand.MS
        second_list = []
        self.sportwearmanager1  = sportwearmanager.SportWearManager(second_list)
        self.sportwearmanager = sportwearmanager.SportWearManager(sportwear_list)


    def test_search_brand(self):
        self.assertEqual(self.sportwearmanager.search_by_brand(self.brand), [])

    def test_sort_by_price(self):
         self.assertEqual(self.sportwearmanager.sort_by_price(enums.SortType.ASC),
                         [self.first_sportshoes, self.second_sportshoes, self.first_tracksuit, self.second_tracksuit])

    def test_add_sportwear(self):
        self.assertTrue(self.sportwearmanager1.add_sportwear(self.third_tracksuit),True)

if __name__ == '__main__':
    unittest.main()
