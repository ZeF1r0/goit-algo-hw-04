def get_cats_info(path):
    cats = []

    try:

        with open(path, 'r', encoding = 'utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat = {
                    'id': cat_id,
                    'name': name,
                    'age': age
                }
                cats.append(cat)

    except FileNotFoundError:
        return cats
    
    except ValueError:
        return cats
    
    return cats

file_path = 'E:/Python_Projects/goit-algo-hw-04/Task_2/cats.txt'
result = get_cats_info(file_path)
print(*result, sep='\n')