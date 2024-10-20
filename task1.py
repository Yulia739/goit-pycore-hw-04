def total_salary(path):
    total = 0
    medium = 0
    dev_count = 0
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")

                total += int(line[1])
                dev_count += 1
                # print(line)
                # print(total)

            medium = total // dev_count
            # print(medium)
        total, medium
        return (total, medium)
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте, чи вказано правильне ім'я файлу.")
    except IOError:
        print(
            "Сталася помилка під час читання файлу. Можливо, файл пошкоджений або немає доступу."
        )


total, medium = total_salary("text1.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {medium}")
