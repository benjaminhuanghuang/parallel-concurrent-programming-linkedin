#!/usr/bin/env python3
""" 
- Lock can be realeased by a different thread than was used to acquire it
- RLock must be released by the same thead that acquired it. 
- RLock must be released the same number of times it was acquired.
"""
import threading

garlic_count = 0
potato_count = 0
# Use reentrant lock, use Lock will cause dead lock
# pencil = threading.Lock()
pencil = threading.RLock()

def add_garlic():
    global garlic_count
    pencil.acquire()
    garlic_count += 1
    pencil.release()

def add_potato():
    global potato_count
    pencil.acquire()
    potato_count += 1
    add_garlic()       # re-enter
    pencil.release()

def shopper():
    for _ in range(10_000):
        add_garlic()
        add_potato()

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
    print('We should buy', potato_count, 'potatoes.')
