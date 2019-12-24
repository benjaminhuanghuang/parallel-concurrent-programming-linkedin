
## API
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
```