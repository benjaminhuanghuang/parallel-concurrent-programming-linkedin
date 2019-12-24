#!/usr/bin/env python3
""" Two shoppers adding items to a shared notepad """

import threading

garlic_count = 0

def shopper():
    global garlic_count
    for _ in range(10_00000):
        # Two threads access same resource
        garlic_count += 1     #  there are 3 steps: read, modify, write back

if __name__ == '__main__':
    barron = threading.Thread(target=shopper)
    olivia = threading.Thread(target=shopper)
    barron.start()
    olivia.start()
    barron.join()
    olivia.join()
    print('We should buy', garlic_count, 'garlic.')
