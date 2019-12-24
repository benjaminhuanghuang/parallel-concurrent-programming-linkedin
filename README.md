# py-concurrency


## Referecen
-[Parallel and Concurrent Programming with Python 1](https://www.linkedin.com/learning/parallel-and-concurrent-programming-with-python-1)
-[Parallel and Concurrent Programming with Python 2](https://www.linkedin.com/learning/parallel-and-concurrent-programming-with-python-2)



## Key points
- Process and thread

- Mutual exclusion
  - Race condition and critical section

- Lock
  - Reentrant lock
  - Try lock
  - Read-write lock
- Liveness
  - Dead lock
  - Starvation
  - Live lock

## Setup
```
$ python3 -m venv venv3

$ . venv3/bin/activate

(venv3)$ pip3 install -r requirements.txt

...
(venv3)$ deactivate
```


## Global interperater lock
Mechamism limits python to only execute ONE thread at a time

CPython has GIL

GIL is not a bottleneck for I/O bound application

CIL can negatively impact performance for CPU bound application

Use the python multiprocessing package to implement parallel operation with multiple process instead of multiple threads.

## Lock vs. RLock
- Lock can be realeased by a different thread than was used to acquire it
- RLock must be released by the same thead that acquired it. 
- RLock must be released the same number of times it was acquired.
- The acquire() method can be called recursively on a RLock, but not on a regular Lock.

## Try Lock / Non-blocking Lock
- Non-blocking lock/acquire method of mutex
- If the mutext is available, lock it and return True. If the mutext is not availabel, immediately return False

## Reader-Writer lock
```
  pip install readerwriterlock
```

## Liveness
- Deadlock
  Eack member is waiting for another memuber to take action
  