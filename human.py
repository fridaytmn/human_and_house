from house import House

class Human:
    default_name = 'No name'
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        #Динамические поля
        # Публиные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None
        
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')
    
    @staticmethod    
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')
    
    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current values: {self.__money}')
        
    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enought money!')
        
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house