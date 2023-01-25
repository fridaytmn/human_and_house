from human import Human
from house import House
from small_house import SmallHouse

def main():
    Human.default_info()
    alexander = Human('Sasha', 27)
    alexander.info()
    small_house = SmallHouse(8_500)
    alexander.buy_house(small_house, 5)
    alexander.earn_money(20_000)
    alexander.buy_house(small_house, 5)
    alexander.info()

main()