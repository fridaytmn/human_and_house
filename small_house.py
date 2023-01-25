from house import House

class SmallHouse(House):
    
    default_area = 40
    
    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)
        self.price = price
    