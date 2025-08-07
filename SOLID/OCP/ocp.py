
class COLOUR:
    RED = 1
    GREEN = 2
    BLUE = 3
    
class SIZE:
    BIG = 1
    MID = 2
    SMALL = 3

class Product:
    def __init__(self, name, colour, size):
        self.name = name
        self.colour = colour
        self.size = size

class Specification():
    def is_satisfied():
        pass

class Filter():
    def filter_product():
        pass
        
class ColourSpecification(Specification):
    def __init__(self, colour):
        self.colour = colour
    
    def is_satisfied(self, product):
        return product.colour == self.colour

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, product):
        return product.size == self.size

class AndSpecification(Specification):
    def __init__(self, *specification_list):
        self.specification_list = specification_list

    def is_satisfied(self, product):
        return all([specification.is_satisfied(product) for specification in self.specification_list])
        
class BetterFilter(Filter):
    def filter_product(self, products, specification):
        filtered_product = []
        for product in products:
            if specification.is_satisfied(product):
                filtered_product.append(product)
        return filtered_product

apple = Product('apple', COLOUR.RED, SIZE.SMALL)
tree = Product('tree', COLOUR.GREEN, SIZE.BIG)
ballon = Product('ballon', COLOUR.RED, SIZE.BIG)
products = [apple, tree, ballon]

green_specification = ColourSpecification(COLOUR.GREEN)
red_specification = ColourSpecification(COLOUR.RED)
small_specification = SizeSpecification(SIZE.SMALL)
red_small_specification = AndSpecification(red_specification, small_specification)
better_filter = BetterFilter()

for product in better_filter.filter_product(products, green_specification):
    print(product.name)
print('==============')
for product in better_filter.filter_product(products, red_specification):
    print(product.name)
print('==============')
for product in better_filter.filter_product(products, small_specification):
    print(product.name)
print('==============')
for product in better_filter.filter_product(products, red_small_specification ):
    print(product.name)
print('==============')
