import datetime
import time
with open('/home/rod/Документы/Python-developer/Python/data_format/newsafr.txt', 'r') as f:
    start_time = time.time()
    #print(time.time(), f.readline(), datetime.datetime.now() )
    #print(start_time, "- %s seconds -" % (time.time() - start_time))

with open('/home/rod/Документы/Python-developer/Python/data_format/newsafr.txt', 'r') as f:
    start_time = time.time()
    print(f.readline())
    a = input('введите что-то')

    print('Время запуска кода - {}\nВремя окончания работы кода - {}'.format(time.localtime(start_time), time.localtime(start_time)), "\nВремя работы - %s seconds " % (time.time() - start_time))

