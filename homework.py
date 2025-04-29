class Fruits:
    def __init__(self, name, variety, origin_country, color, weight, price):
        self.name = name                 # название фрукта (например, 'яблоко')
        self.variety = variety           # сорт (например, 'Голден')
        self.origin_country = origin_country  # страна происхождения (например, 'Турция')
        self.color = color               # цвет (например, 'зеленый')
        self.weight = weight             # вес 1 кг фрукта  (в кг)
        self.price = price # цена за кг

    def start_the_Sale(self):
        print(f"Сезон фруктов: {self.name} ({self.variety}) из {self.origin_country}, цвет: {self.color}, {self.weight} кг — по цене {self.price} сом начался.")
        print("Поторопитесь! Свежие фрукты уже в продаже.")
    def stop_the_Sale(self):
        print(f"Продажа {self.name} ({self.variety}) завершена. Ожидайте новое поступление!")

class Apple (Fruits):
    def __init__(self, name, variety, origin_country, color, weight, price, taste, shelf_life):
        super().__init__(name, variety, origin_country, color, weight, price)
        self.taste = taste
        self.shelf_life = shelf_life

    def info(self):
        print(f"Яблоко имеет вкус: {self.taste}. Хранится до {self.shelf_life} дней в прохладном месте.")

class Cherry (Fruits):
     def __init__(self, name, variety, origin_country, color, weight, price, use, form):
        super().__init__(name, variety, origin_country, color, weight, price)
        self.use = use
        self.form = form
        
     def benefits(self):
        print(f"Гилас богат антиоксидантами и {self.use} в косметологии. Форма продукта: {self.form}.")

class Kiwi (Fruits):
     def __init__(self, name, variety, origin_country, color, weight, price, vitamins, feature):
        super().__init__(name, variety, origin_country, color, weight, price)
        self.vitamins = vitamins
        self.feature = feature
     def vitamin_info(self):
        kiwi = Kiwi("Киви", "Золотой", "Италия", "зелёный", 1.0, 280, 92, "Высокое содержание антиоксидантов")
        
class Banana (Fruits):
    def __init__(self, name, variety, origin_country, color, weight, price, potassium_level, ferrium_level):
        super().__init__(name, variety, origin_country, color, weight, price)
        self.potassium_level = potassium_level
        self.ferrium_level = ferrium_level
    def energy_boost(self):
        print(f"Банан — быстрый источник энергии и содержит {self.potassium_level} мг калия на 100 г и  {self.ferrium_level} мг железа на 100 г")

class Orange (Fruits):
    def __init__(self, name, variety, origin_country, color, weight, price, juice_yield):
        super().__init__(name, variety, origin_country, color, weight, price)
        self.juice_yield = juice_yield
    def juice_info(self):
        print(f"С {self.weight} кг апельсинов получается примерно {self.juice_yield} мл сока.")



Fruits = Fruits("Фрукты", "сорт", "олко", "ар кандай тусто", 5.2,  500)
Fruits.start_the_Sale()
Fruits.stop_the_Sale()

apple = Apple("Яблоко", "Голден", "Кыргызстан", "зеленое", 1.0, 80, "сладкий", 30)
apple.start_the_Sale()
apple.stop_the_Sale()
apple.info()

cherry = Cherry("Гилас", "Крупноплодный", "Кыргызстан", "кызыл", 1.0, 350, "применяется", "вяленая")
cherry.start_the_Sale()
cherry.stop_the_Sale()
cherry.benefits()

kiwi = Kiwi("Киви", "Золотой", "Италия", "зелёный", 1.0, 280, 92, "Высокое содержание антиоксидантов")
kiwi.start_the_Sale()
kiwi.stop_the_Sale()
kiwi.vitamin_info()

banana = Banana("Банан", "Кавендиш", "Эквадор", "жёлтый", 1.2, 75, 358, 234)
banana.start_the_Sale()
banana.stop_the_Sale()
banana.energy_boost()

orange = Orange("Апельсин", "Навел", "Турция", "оранжевый", 1.5, 95, 900)
orange.start_the_Sale()
orange.stop_the_Sale()
orange.juice_info()
