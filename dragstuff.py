# Goal is to make dragging ingredient, turning it upside down, and putting it on conveyer belt. Generate an image get filenmae for image, return an Iengredient(image)



def IngredientclickedOn(event, data):
    if 300 < event.x < 467 and 263 < event.y < 414:
        return Ingredient("patty.png")
    elif 487 < event.x < 603 and 270 < event.y < 411:
        return Ingredient("mushroom.png")
    return None
