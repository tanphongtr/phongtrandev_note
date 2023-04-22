# Python program to illustrate the concept
# of threading
import threading
import os
# import sleep
from time import sleep
import time

def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))
    print('Task 1 sleeping for 2 seconds')
    sleep(5)

def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))
    sleep(8)


if __name__ == "__main__":

    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')
    t3 = threading.Thread(target=task1, name='t3')
    t4 = threading.Thread(target=task2, name='t4')
    t5 = threading.Thread(target=task1, name='t5')
    t6 = threading.Thread(target=task2, name='t6')
    t7 = threading.Thread(target=task1, name='t7')
    t8 = threading.Thread(target=task2, name='t8')
    t9 = threading.Thread(target=task1, name='t9')
    t10 = threading.Thread(target=task2, name='t10')


    start_t = time.perf_counter()
    # starting threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()

    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()

    print(time.perf_counter() - start_t, "seconds")

    print("All threads finished execution!")
