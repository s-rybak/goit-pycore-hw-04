def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.rstrip("\n").split(',')
                cats.append({'id': id, 'name': name, 'age': age})
        return cats
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не знайдений")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

print(get_cats_info('cats.txt'))