def parse_recipes(file_path):
    """
    Читает файл с рецептами и создает словарь cook_book.
    :param file_path: путь к файлу с рецептами
    :return: словарь cook_book
    """
    cook_book = {}
    with open(file_path, encoding='utf-8') as file:
        while line := file.readline().strip():
            dish_name = line  
            ingredients_count = int(file.readline().strip())  
            ingredients = []
            
            for _ in range(ingredients_count):
                ingredient = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                })
            
            cook_book[dish_name] = ingredients
            file.readline()  
    
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    
    shop_list = {}
    
    for dish in dishes:
        if dish not in cook_book:
            print(f"Блюдо '{dish}' отсутствует в кулинарной книге!")
            continue
        
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            
            if name in shop_list:
                shop_list[name]['quantity'] += quantity
            else:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
    
    return shop_list


def main():
   
    file_path = 'recipes.txt'
    
    try:
        
        cook_book = parse_recipes(file_path)
        print("Кулинарная книга:")
        for dish, ingredients in cook_book.items():
            print(f"{dish}: {ingredients}")
        
        
        dishes_to_prepare = ['Запеченный картофель', 'Омлет']
        person_count = 2
        shop_list = get_shop_list_by_dishes(dishes_to_prepare, person_count, cook_book)
        
        print("\nСписок покупок:")
        for ingredient, details in shop_list.items():
            print(f"{ingredient}: {details}")
    
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")


if __name__ == "__main__":
    main()


import os

def merge_files_sorted_by_lines(folder_path, output_file):
   
    files = []

    
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8') as f:
                lines = f.readlines()
                files.append({
                    'file_name': file_name,
                    'lines': lines,
                    'line_count': len(lines)
                })

    
    sorted_files = sorted(files, key=lambda x: x['line_count'])

    
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_data in sorted_files:
            out_f.write(f"{file_data['file_name']}\n")
            out_f.write(f"{file_data['line_count']}\n")
            out_f.writelines(file_data['lines'])
            out_f.write('\n')  

    print(f"Файлы объединены в {output_file}")


def main():
    
    folder_path = 'files'
    
    output_file = 'result.txt'

    try:
        
        merge_files_sorted_by_lines(folder_path, output_file)
    except FileNotFoundError:
        print(f"Папка {folder_path} не найдена.")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
