class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = 0

    def edit_category(self, new_category):
        self.category = new_category

    def edit_price(self, new_price):
        self.price = new_price

    def set_sale(self, sale):
        if 0 <= sale <= 100:
            self.sale = sale
        else:
            raise ValueError("Скидка должна быть в диапазоне от 0 до 100.")

    def cancel_sale(self):
        self.sale = 0

    def get_price(self):
        return self.price * (1 - self.sale / 100)

    def __repr__(self):
        return (f"Product(name='{self.name}', category='{self.category}', "
                f"price={self.price}, sale={self.sale})")
