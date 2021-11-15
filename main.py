import classes
from classes import enums, sportwearmanager, sportwear, track_suit, sportshoes
def main():

    first_sportshoes = classes.sportshoes.SportShoes(42,1500,classes.enums.Brand.NIKE, classes.enums.Color.BLUE, classes.enums.Sex.UNISEX)
    second_sportshoes = classes.sportshoes.SportShoes(38,2000,classes.enums.Brand.ADIDAS, classes.enums.Color.RED, classes.enums.Sex.MALE)

    first_tracksuit = classes.track_suit.TrackSuit(42,100,3000,classes.enums.Brand.PUMA, classes.enums.Color.WHITE, classes.enums.Sex.FEMALE)
    second_tracksuit = classes.track_suit.TrackSuit(38,70,3500,classes.enums.Brand.ASICS, classes.enums.Color.PURPLE, classes.enums.Sex.MALE)
    third_tracksuit = classes.track_suit.TrackSuit(
        38, 70, 3500, classes.enums.Brand.ASICS, classes.enums.Color.PURPLE, classes.enums.Sex.MALE)
    sportwear_list = []
    manager = classes.sportwearmanager.SportWearManager(sportwear_list)

    manager.add_sportwear(second_tracksuit)
    manager.add_sportwear(first_sportshoes)
    manager.add_sportwear(second_sportshoes)
    manager.add_sportwear(third_tracksuit)

    for items in manager.get_sportwear_list():
         print(items)
    # for items in manager.search_by_brand(enums.Brand.ADIDAS):
    #     print(items)
    # for items  in manager.sort_by_price(enums.SortType.ASC):
    #     print(items)

if __name__ == '__main__':
    main()
