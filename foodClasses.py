# Mckenna Brown

class Food():
    def __init__(self, ingredients, data):
        self.recipe = ingredients  # a list. can have repeats
        # ordered. must be put on in this order
        self.ingredients = []
        self.x = data.currFoodX
        self.y = data.currFoodY


    def addIngredient(self, ingredient):
        i = len(self.ingredients)
        if self.recipe[i] != ingredient:  # can't drag that
            return False
        else:
            self.ingredients.append(ingredient)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, data):
        for ingredient in self.ingredients:
            screen.blit(ingredient.img, (self.x, self.y))


class Ingredient():
    def __init__(self, img):
        self.img = pygame.image.load(img)

    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.img == other.img
