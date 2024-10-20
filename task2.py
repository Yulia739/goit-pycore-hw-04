def get_cats_info(path):
    '''
    This function create a list of cats dictionary
    '''
    cats_info = []
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")

                cats_dict = {}
                cats_dict["id"] = line[0]
                cats_dict["name"] = line[1]
                cats_dict["age"] = line[2]
                cats_info.append(cats_dict)
                # print(cats_dict)
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте, чи вказано правильне ім'я файлу.")
    except IOError:
        print(
            "Сталася помилка під час читання файлу. Можливо, файл пошкоджений або немає доступу."
        )


cats_info = get_cats_info("text2.txt")
print(cats_info)
