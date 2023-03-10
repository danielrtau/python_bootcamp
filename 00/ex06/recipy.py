import os
import time

def new_recipy(name, ingredients, meal, prep_time):
    recipy = {}
    recipy['name'] = name
    recipy['ingredients'] = ingredients
    recipy['meal'] = meal
    recipy['prep_time'] = prep_time
    return recipy

def intro():
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print(" 1: Add a recipe\n 2: Delete a recipe\n 3: Print a recipe \n 4: Print the cookbook\n 5: Quit")
    option = int(input("Please select an option: "))
    try:
        assert type(option) is int, "pruebs"

        if option == 1:
            os.system('clear')
            add_recipe()
        if option == 2:
            os.system('clear')
            del_recipe()
            intro()
        if option == 3:
            print_recipe()
        if option == 4:
            os.system('clear')
            print_cookbook()
        if option == 5:
            exit()
        if option < 1 or option > 5:
            os.system('clear')
            input("Invalid option, press Enter to continue...")
            os.system('clear')
        intro()

    except ValueError as msg:
        print(msg)
        intro()

def print_cookbook():
    for i in recetas:
        print("\nRecipe for: " + i['name'])
        print("\tIngredients list:", end=" ")
        for j in i['ingredients']:
            if j != i['ingredients'][-1]:
                print(j, end=", ")
            else:
                print(j)
        print("\tTo be eaten for: " + i['meal'])
        print("\tTakes " + str(i['prep_time']) + " minutes of cooking")
    input("\nPress Enter to continue...")
    os.system('clear')

def add_recipe():
    a1 = str(input("Name: "))
    a2 = []
    aux_a2 = str(input("Ingredients (type 'done' to finish): "))
    while aux_a2 != "done":
        a2.append(aux_a2)
        aux_a2 = str(input("Ingredients (type 'done' to finish): "))
    a3 = str(input("Type of meal: "))
    a4 = int(input("Preparation cooking: "))
    nr = new_recipy(a1, a2, a3, a4)
    recetas.append(nr)
    return

def del_recipe():
    n1 = 1
    for i in recetas:
        print(str(n1) + ". " + i['name'])
        n1 += 1
    dele = int(input("Select recipe to be deleted: "))
    recetas.pop(dele - 1)
    return

def print_recipe():
    n1 = 1
    for i in recetas:
        print(str(n1) + ". " + i['name'])
        n1 += 1
    prnt = int(input("Select recipe to print: "))
    #print(recetas[prnt - 1])
    i = recetas[prnt - 1]
    print("\nRecipe for: " + i['name'])
    print("\tIngredients list:", end=" ")
    for j in i['ingredients']:
        if j != i['ingredients']:
            print(j, end=", ")
        else:
            print(j)
    print("\tTo be eaten for: " + i['meal'])
    print("\tTakes " + str(i['prep_time']) + " minutes of cooking")
    input("\nPress Enter to continue...")
    os.system('clear')

if __name__ == '__main__':
    os.system('clear')
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
    intro()
    #nr = new_recipy("tarta", a2, a3, a4)
    #recetas.append(nr)
    #recetas.pop(0)

