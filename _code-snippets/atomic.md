### C++
```
  #include <atomic>

  std::atomic<unsigned int> garlic_count(0);

  void shopper() {
    for (int i=0; i<10000000; i++) {
        garlic_count++;    // critical section
    }
  }
```