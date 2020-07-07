## Reentrant Mutex
Internally, the reentrant mutex keeps track of how many times it's been locked by the owning thread and it has to be unlocked an equal number of times before another thread can lock it.


