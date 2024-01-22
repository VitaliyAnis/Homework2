def work_with_phonebook():
    choice = show_menu()

    phone_book = read_txt('phon.txt')

    while (choice != 7):

        if choice == 1:
            print(show_phonebook(phone_book))
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new  number ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            lastname = input('lastname ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 5:
            number = input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            # user_data = input("Введите фамилию: ") + input("Введите имя: ") + input("Введите номер телефона: ") + input("Введите описание: ")
            user_data = input("Введите данные абонента: ")
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)

        choice = show_menu()



def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента по фамилии\n"
          "4. Удалить абонента по фамилии\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить абонента в справочник\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def read_txt(filename):
    phone_book = []

    fields = ['Last_name', 'First_name', 'Number', 'description']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            values = line.strip().split(',')
            record = dict(zip(fields, values))
            phone_book.append(record)


    return phone_book

# def user_data(phone_book):
#     last_name = input("Введите фамилию: ")
#     first_name = input("Введите имя: ")
#     number = input("Введите номер телефона: ")
#     opisanie = input("Введите описание абонента: ")
#
#     return new_user_data


def add_user(phone_book, user_data):
    fields = ['Last_name', 'First_name', 'Number', 'description']

    user_values = user_data.split(',')


    if len(user_values) == len(fields):
        # Введенные данные содержат правильное количество полей
        record = dict(zip(fields, user_values))
        phone_book.append(record)
        print("Пользователь успешно добавлен.")
    else:
        print("Некорректные данные. Пожалуйста, введите все необходимые поля.")

def write_txt(filename, phone_book):

    with open('phon.txt','w' ,encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')


def show_phonebook(phone_book):
    print("\nВесь справочник:")
    for entry in phone_book:
        print("Фамилия:", entry["Last_name"])
        print("Имя:", entry["First_name"])
        print("Номер телефона:", entry["Number"])
        print("Описание:", entry["description"])
        print("----------------------")










work_with_phonebook()