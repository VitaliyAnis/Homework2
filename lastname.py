def write_txt(filename, phone_book):

    with open('phon.txt','w' ,encoding='utf-8') as phout:



user_data = input('new data ')
add_user(phone_book, user_data)
write_txt('phon.txt', phone_book)