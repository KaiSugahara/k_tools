import datetime
import codecs

def print2File(*text, file_name="./log.txt", is_init=False, include_time=False):

    if is_init:
        
        print(file=codecs.open(file_name, 'w', 'utf-8'), end="")

    else:

        if include_time:
            print(str(datetime.datetime.now())+':', *text)
            print(str(datetime.datetime.now())+':', *text, file=codecs.open(file_name, 'a', 'utf-8'))
        else:
            print(*text)
            print(*text, file=codecs.open(file_name, 'a', 'utf-8'))