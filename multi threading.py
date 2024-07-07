import threading
from threading import *
from time import sleep
class first_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"this is first thread")
            sleep(1)
class second_thread(Thread):
    def run(self):
        for i in range(1,10):
            print(i,"this is second thread")
            sleep(1)
a=first_thread()
b=second_thread()
a.run()
sleep(1)
b.run()
sleep(1)

a.start()
print(a.is_alive())
b.start()
print(b.is_alive())

a.join()
print(a.is_alive())
b.join()
print(b.is_alive())

print(threading.current_thread().getName())
