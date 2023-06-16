from threading import Thread

def hello():
    for i in range(100):
        print('hello')

def world():
    for i in range(100):
        print('world')

thread1 = Thread(target=hello)
thread2 = Thread(target=world)

thread1.start()  # Старт потока №1
thread2.start()  # Старт потока №2

thread1.join()
thread2.join()

# прогресс бар
import sys
import time

for i in range(11):
    sys.stdout.write("[ % -1s] %d %%" % ('=' * i, 10 * i))
    sys.stdout.write('\n')
    time.sleep(0.30)

