
## API
```
import os
import threading

# get current process id
os.getpid()   

# thread count in process
threading.active_count()           

# iterate threads
for thread in threading.enumerate():             
    print(thread)

# Create thread
threading.Thread(target=cpu_waster).start()

```