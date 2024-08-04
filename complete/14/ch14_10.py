import threading
import time

def print_numbers():
    for i in range(6):
        print(f"number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'abcd':
        print(f"letter: {letter}")
        time.sleep(2)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All Thread Completed")




