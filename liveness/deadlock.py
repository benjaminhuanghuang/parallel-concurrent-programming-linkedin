#!/usr/bin/env python3
""" Three philosophers, thinking and eating sushi """

import threading

chopstick_a = threading.Lock()   # First priority
chopstick_b = threading.Lock()   # Second priority
chopstick_c = threading.Lock()   # Third priority
sushi_count = 500

def philosopher(name, first_chopstick, second_chopstick):
    global sushi_count
    while sushi_count > 0: # eat sushi until it's all gone
        first_chopstick.acquire()
        second_chopstick.acquire()

        if sushi_count > 0:
            sushi_count -= 1
            print(name, 'took a piece! Sushi remaining:', sushi_count)

        second_chopstick.release()
        first_chopstick.release()
        
if __name__ == '__main__':
    # Each thread shoud acquire the higher pririty lock first!
    threading.Thread(target=philosopher, args=('Barron', chopstick_a, chopstick_b)).start()
    threading.Thread(target=philosopher, args=('Olivia', chopstick_b, chopstick_c)).start()
    # threading.Thread(target=philosopher, args=('Steve', chopstick_c, chopstick_a)).start()  # Cause dead lock
    threading.Thread(target=philosopher, args=('Steve', chopstick_a, chopstick_c)).start()
