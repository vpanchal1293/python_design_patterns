
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
   
class ProductFilter:
    def filter_by_colour(products, colour):
        filtered_product = []
        for product in products:
            if product.colour == colour:
                filtered_product.append(product)
        return filtered_product
    
    def filter_by_size(products, size):
        filtered_product = []
        for product in products:
            if product.size == size:
                filtered_product.append(product)
        return filtered_product
        
    def filter_by_colour_size(products, colour, size):
        filtered_product = []
        for product in products:
            if ((product.size == size) and (product.colour == colour)):
                filtered_product.append(product)
        return filtered_product
        
product_1 = Product('p1', COLOUR.RED, SIZE.SMALL)
product_2 = Product('p2', COLOUR.GREEN, SIZE.BIG)
product_3 = Product('p3', COLOUR.BLUE, SIZE.MID)
product_4 = Product('p4', COLOUR.RED, SIZE.BIG)
products = [product_1, product_2, product_3, product_4]

green_filter = ProductFilter.filter_by_colour(products, COLOUR.GREEN)
for product in green_filter:
    print(product.name)

red_big_filter = ProductFilter.filter_by_colour_size(products, COLOUR.RED, SIZE.BIG)
for product in red_big_filter:
    print(product.name)
