

## Python
```
import threading

pencil = threading.Lock()

  pencil.acquire()
    #
    # critical section
    #
  pencil.release()

```


## Java
```


```

## C++
```
#include <mutex>

std::mutex pencil;

  pencil.lock();
    //
    // critical section
    //
  pencil.unlock();

```