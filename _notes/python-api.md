
## Thread
```
import os
import threading
import time

# get current process id
os.getpid()   

# thread count in process
threading.active_count()           

# iterate threads
for thread in threading.enumerate():             
    print(thread)

# Create thread
threading.Thread(target=cpu_waster, name='Barron').start()
# get thread name
name = threading.current_thread().getName()

# sleep 1 second
time.sleep(1)    


#
# Thread class
#
class ChefOlivia(threading.Thread):
  def __init__(self):
    super().__init__()

  def run(self):
    time.sleep(3)

```


## Lock
```
# Lock
pencil = threading.Lock()
pencil.acquire()
  garlic_count += 1
pencil.release()


# reentrant lock
pencil = threading.RLock()


# Read write lock
marker = rwlock.RWLockFair()

read_marker = marker.gen_rlock()    ## Reader Lock
write_marker = marker.gen_wlock()   ## Write Lock

```

## Condition
```
import threading

slowcooker_lid = threading.Lock()
soup_taken = threading.Condition(lock=slowcooker_lid)

while not (SOME CONDITION)
  soup_taken.wait()
  #do something
  soup_taken.notify_all()
```

