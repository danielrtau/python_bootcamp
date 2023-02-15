def new_recipy(name, ingredients, meal, prep_time):
    recipy = {}
    recipy['name'] = name
    recipy['ingredients'] = ingredients
    recipy['meal'] = meal
    recipy['prep_time'] = prep_time
    return recipy

if __name__ == '__main__':
    ingredients = []
    ingredients += ["ham", "bread", "cheese", "tomatoes"]
    r1 = new_recipy("Sandwich", ingredients, "lunch", 10)
    ingredients = []
    ingredients += ["flour", "sugar", "eggs"]
    r2 = new_recipy("Cake", ingredients, "dessert", 60)
    ingredients = []
    ingredients += ["avocado", "arugula", "tomatoes"]
    r3 = new_recipy("Salad", ingredients, "lunch", 15)
    for i in r1['ingredients']:
        if i == r1['ingredients'][-1]:
            print(i)
        else:
            print(i, end=", ")
    print(r1['ingredients'])
    print(r2)
    print(r3)
