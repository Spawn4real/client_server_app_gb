enc_str = ('разработка', 'администрирование', 'protocol', 'standart')


def enc_dec_str(words):
    for i in words:
        enc_str_bytes = i.encode('utf-8')
        print(enc_str_bytes)
        dec_bytes_str = enc_str_bytes.decode('utf-8')
        print(dec_bytes_str)
    return words


enc_dec_str(enc_str)