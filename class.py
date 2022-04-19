# Пункт a)
# Описание класса: у телефона есть модель и марка, можно узнать о наличии телефона в интернет-магазине
# Класс: Phone
# Атрибуты объектов данного класса:
# - model
# - brand
# Методы объектов данного класса:
# - is_awailable()
class Phone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def is_awailable(self):
        print(f"Смартфон {self.brand} {self.model} есть в продаже за {self.price} рублей.")


phone = Phone(brand = 'Xiomi', model = 'Mi 10 Pro', price = '50 000')
print("Brand:", phone.brand)
print("Model:", phone.model)
print("Price:", phone.price)
phone.is_awailable()
