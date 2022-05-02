from chardet import detect

create_file = open('text.txt', 'w', encoding='utf-8')
create_file.write('сетевое программирование, сокет, декоратор')
create_file.close()


def encode_file(file):
    with open(file, 'rb' ) as my_file:
        content = my_file.read()
    encoding = detect(content)['encoding']
    print('encoding: ', encoding)
    with open(file, encoding=encoding) as my_file_n:
        for elem in my_file_n:
            print(elem, end='')
        print()


encode_file('text.txt')