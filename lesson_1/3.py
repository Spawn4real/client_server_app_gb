words_str = ('класс', 'atribute', 'type', 'функция')


def byte_words_error(words):
    for i in words:
        try:
            byte_str = f"b'{i}'"
            print(type(eval(byte_str)))
            print(byte_str)
            print(len(byte_str))
        except SyntaxError:
            print('Cимволы не относятся к ASCII')


byte_words_error(words_str)
