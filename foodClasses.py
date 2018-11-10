# Mckenna Brown

class Food():
    def __init__(self, ingredients):
        self.recipe = ingredients  # a list. can have repeats
        # ordered. must be put on in this order
        self.ingredients = []

    def addIngredient(self, ingredient):
        i = len(self.ingredients)
        if self.recipe[i] != ingredient:  # can't drag that
            return False
        else:
            self.ingredients


class Ingredient():
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.img == other.img
