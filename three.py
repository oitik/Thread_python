import threading
counter = 0


def increase(num):
    global counter
    for _ in range(num):
        counter = counter + 1


def decrease(num):
    global counter
    for _ in range(num):
        counter = counter - 1


t1 = threading.Thread(target=increase, args=[1000000])
t2 = threading.Thread(target=decrease, args=[1000000])
t1.start()
t2.start()
t1.join()
t2.join()

print(counter)
