"""
класстын 4 туру бар полиморфизм, наследования, абтракция, инкапсуляция
"""
##oop

# class Dog:
#     def __init__(self, name, age, year):
#         self.name = name
#         self.age = age
#         self.year = year

#     def bark(self):
#         return f"{self.name} age {self.age} , {self.year} Woof!"
    
# my_dog = Dog("Buddy", 3, 2022)
# print(my_dog.bark())


# class Cars:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

# def start_the_engine(self):
#     print(f"Двигатель автомобиля {self.brand} {self.model} запущеню ")

# def stop_the_engine(self):
#     print(f"Двигатель автомобиля {self.brand} {self.model} остановлен ")

# class ElectroCar (Cars):
#     def charge(self):
#         print(f"Электромобиль {self.brand} {self.model} заряжается ")

# # Создаем объект класса Cars
# cars = Cars("Toyota", "Camry", 2020)
# cars.start_the_engine()
# cars.stop_the_engine()


# ## Создаем объект класса ElectroCar
# electro_cars = ElectroCar("Tesla", "Model", 2022)
# electro_cars.start_the_engine()
# electro_cars.stop_the_engine()
# electro_cars.charge()



class Laptops:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def start_the_Sale(self):
        print(f"Cатуу {self.brand} {self.model} {self. year} {self.color}  {self.price} башталды")

    def stop_the_Sale(self):
        print(f"Сатуу {self.brand} {self.model} {self. year} {self.color}  {self.price} журуп жатат")

class Dell (Laptops):
    def processor (self):
        print(f"Ноутбук Dell {self.brand} {self.model} - {self.year}-жылы чыккан, {self.color} түстө, баасы {self.price}. "
              f"Бул модель Intel Core i5 процессору жана 8GB RAM менен жабдылган, иш үчүн абдан ыңгайлуу.")


class Asus (Laptops):
    def VideoCard (self):
        print(f"Ноутбук Asus {self.brand} {self.model} - {self.year}-жылы чыккан, {self.color} түстө, баасы {self.price}. "
              f"Бул ноутбук оюнга ылайыктуу, анткени ал күчтүү видеокарта жана жогорку жаңылануу ылдамдыгы менен келет.")


class Samsung (Laptops):
    def design (self):
        print(f"Ноутбук Samsung {self.brand} {self.model} - {self.year}-жылы чыккан, {self.color} түстө, баасы {self.price}. "
              f"Бул модель дизайны менен айырмаланат жана AMOLED дисплей менен жабдылган.")

## Создаем объект класса Loptops
Laptops = Laptops("Acer", "13420H", 2021, "кара жана ак", "70 000 cом")
Laptops.start_the_Sale()
Laptops.stop_the_Sale()


## Создаем объект класса Dell
Dell = Dell("Dell", "Vostro 14 3000", 2022, "кара", "40 000 сом")
Dell.start_the_Sale()
Dell.stop_the_Sale()
Dell.processor()

## Создаем объект класса Asus
Asus = Asus("Asus", "7435HS", 2023, "ак", "69 000")
Asus.start_the_Sale()
Asus.stop_the_Sale()
Asus.VideoCard()


## Создаем объект класса Samsung
Samsung = Samsung("Samsung", "Galaxy Book3 Pro NP960XFG-KA2", 2024, "кызыл", "140 000 сом")
Samsung.start_the_Sale()
Samsung.stop_the_Sale()
Samsung.design()
