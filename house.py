class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
        
    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price
        