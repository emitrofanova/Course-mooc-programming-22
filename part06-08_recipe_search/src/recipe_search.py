# Write your solution here
def search_by_name(filename: str, word: str):
    with open(filename) as recipes:
        rec = recipes.read()
        rec = rec.split("\n")
        recipes_list = []
        recipe = []
        for line in rec:
            if line == "":
                recipes_list.append(recipe)
                recipe = []
            else:
                recipe.append(line)
    answ = []
    for recipe_cnt in recipes_list:
        if word.lower() in recipe_cnt[0].lower():
            answ.append(recipe_cnt[0])
    return answ
       
def search_by_time(filename: str, prep_time: int):
    with open(filename) as recipes:
        rec = recipes.read()
        rec = rec.split("\n")
        recipes_list = []
        recipe = []
        for line in rec:
            if line == "":
                recipes_list.append(recipe)
                recipe = []
            else:
                recipe.append(line)
    answ = []
    for recipe_cnt in recipes_list:
        if int(recipe_cnt[1]) < prep_time:
            answ.append(f"{recipe_cnt[0]}, preparation time {recipe_cnt[1]} min")
    return answ

def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as recipes:
        rec = recipes.read()
        rec = rec.split("\n")
        recipes_list = []
        recipe = []
        for line in rec:
            if line == "":
                recipes_list.append(recipe)
                recipe = []
            else:
                recipe.append(line)
    answ = []
    for recipe_cnt in recipes_list:
        for ingredients in recipe_cnt[2:]:
            if ingredient in ingredients:
                answ.append(f"{recipe_cnt[0]}, preparation time {recipe_cnt[1]} min")
    return answ

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)
    
    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)
