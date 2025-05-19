recipes = []

def show_menu():
    print("\n1. Показать все рецепты")
    print("2. Добавить рецепт")
    print("3. Выход")

def show_recipes():
    if not recipes:
        print("Рецептов пока нет.")
    else:
        print("\nСписок рецептов:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe}")

def add_recipe():
    title = input("Введите название рецепта: ")
    recipes.append(title)
    print("Рецепт добавлен!")

while True:
    show_menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        show_recipes()
    elif choice == "2":
        add_recipe()
    elif choice == "3":
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
