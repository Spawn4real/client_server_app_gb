import chardet
import subprocess
import platform

web_link = ('yandex.ru', 'youtube.com')


def ping_web(web):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '2', web]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

        return web


for i in web_link:
    ping_web(i)


import locale
default_encoding = locale.getpreferredencoding()
print(default_encoding)
