last_name = str(input("Введите фамилию:"))
first_name = str(input("Введите имя:"))
number = str(input("Введите номер телефона:"))
opisanie = str(input("Введите описание абонента:"))
list_data = [last_name, first_name, number, opisanie]

print(list_data)


fields = ['Last_name', 'First_name', 'Number', 'description']



len(list_data) == len(fields)
print(len(list_data))
print(len(fields))
#
# # f"{last_name}, {first_name}, {number}, {opisanie}"