# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Доп: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def print_file(file_path):
    with open(file_path, "r") as f:
        print(f.read())


def write_contact(file_path):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open(file_path, "a") as f:
        f.write(f"{name} {surname} {patronymic} - {phone_number}\n")


def change_contact(file_path):
    print("Введите пользователя, которого хотите изменить: ")
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    print("Введите новое значение: ")
    name2 = input("Введите новое имя: ")
    surname2 = input("Введите новую фамилию: ")
    patronymic2 = input("Введите новое отчество: ")
    phone_number2 = input("Введите новый номер телефона: ")

    with open(file_path, "r") as f:
        result = ""
        old_contact = f"{name} {surname} {patronymic} - {phone_number}"
        new_contact = f"{name2} {surname2} {patronymic2} - {phone_number2}"
        for i in f.readlines():
            if old_contact in i:
                result += new_contact + "\n"
                continue
            result += i
        save_file(file_path, result)


def delete_contact(file_path):
    print("Введите пользователя, которого хотите удалить: ")
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    with open(file_path, "r") as f:
        result = ""
        old_contact = f"{name} {surname} {patronymic} - {phone_number}"
        for i in f.readlines():
            if old_contact in i:
                continue
            result += i
        save_file(file_path, result)


def search_contact(file_path):
    key = input("Введите значение для поиска:")
    with open(file_path, "r") as f:
        for i in f.readlines():
            if key in i:
                print(i)


def save_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)


def main():
    while True:
        print("Инсрукция")
        print("1. Записать номер в справочник")
        print("2. Вывести данные из справочника")
        print("3. Поиск по справочнику")
        print("4. Выход")
        print("5. Изменить данные")
        print("6. Удалить данные")

        choice = input("Введите номер действия: ")
        file_path = 'text.txt'
        if choice == "1":
            write_contact(file_path)
        elif choice == "2":
            print_file(file_path)
        elif choice == "3":
            search_contact(file_path)
        elif choice == "5":
            change_contact(file_path)
        elif choice == "6":
            delete_contact(file_path)
        else:
            break


