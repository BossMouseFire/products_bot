import json


class Analyze:

    def __init__(self):
        with open('products.json') as json_file:
            self.data = json.load(json_file)

    def check_lactose_product(self, product_name):
        return product_name in map(lambda elem: elem["productName"], self.data["lactoseFree"])

    def check_gluten_product(self, product_name):
        return product_name in map(lambda elem: elem["productName"], self.data["glutenFree"])

    def get_lactose_products(self):
        return self.data["lactoseFree"]

    def get_gluten_products(self):
        return self.data["glutenFree"]

    def get_variations_text(self, type_name, product_name):
        list_product = list(map(lambda elem: elem["productName"], self.data[type_name]))
        index = list_product.index(product_name)
        variations = self.data[type_name][index]["variations"]

        result = ""
        for idx, value in enumerate(variations, 1):
            result += "{:d}. {:s}\n\n".format(idx, value)

        return result
