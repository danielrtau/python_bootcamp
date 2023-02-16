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
    recetas = []
    recetas.append(r1)
    recetas.append(r2)
    recetas.append(r3)
    a1 = "pizza"
    a2 = ["masa", "jamon"]
    a3 = "dinner"
    a4 = 25
    nr = new_recipy(a1, a2, a3, a4)
    recetas.append(nr)
    nr = new_recipy("tarta", a2, a3, a4)
    recetas.append(nr)
    recetas.pop(0)
    for i in recetas:
            print(i['name'])
            for j in i['ingredients']:
                if j != i['ingredients'][-1]:
                    print(j, end=", ")
                else:
                    print(j)
