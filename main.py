# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


        #module_7_1.py
    #Задача "Учёт товаров"


from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name #азвание продукта
        self.weight = weight #общий вес товара
        self.category = category # категория товара
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop(Product):
    def __init__(self, name, weight, category, __file_name='products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name
    def get_products(self):
        file = open(self.__file_name, 'r')
        st = file.read()
        file.close()
        print(f'{st}')
    def add(self, *products):
        for i in products:
            s = (str(i))
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if s in f:
                print(f'Продукт {s} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{s}')
                file.close()

s1 = Shop('',0 , '')
p1 = Product('banana', 0.5, 'fruit')
p2 = Product('canfets', 2.4, 'confectionery products')
p3 = Product('banana', 2.7, 'fruit')
p4 = Product('apple', 0.5, 'fruit')
p5 = Product('coffee', 0.1, 'groceries')
print(p2)  # __str__

s1.add(p1, p2, p3,p4,p5)

print(s1.get_products())

s1.get_products()
