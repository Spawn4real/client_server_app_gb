words_str = ('method', 'function', 'class')


def byte_words(words):
    for i in words:
        byte_str = f"b'{i}'"
        print(byte_str)
        print(type(eval(byte_str)))
        print(len(byte_str))
    return words


byte_words(words_str)

