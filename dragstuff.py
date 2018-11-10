# Goal is to make dragging ingredient, turning it upside down, and putting it on conveyer belt. Generate an image get filenmae for image, return an Iengredient(image)

import pygame

def IngredientclickedOn(event, data):
    if 300 < pygame.mouse.get_pos()[0] < 467 and 263 < pygame.mouse.get_pos()[1] < 414:
        return Ingredient("patty.png")
    elif 487 < pygame.mouse.get_pos()[0] < 603 and 270 < pygame.mouse.get_pos()[1] < 411:
        return Ingredient("mushroom.png")
    return None
