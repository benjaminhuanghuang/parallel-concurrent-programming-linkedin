# Global Interpreter Lock
- Mechanism that limits Python to only execute one thread at a time
- CPython has GIL
- GIL is not a bottleneck for I/O intensive app:
- GIL is a bottleneck for CPU intensive app
- Python multiprocessing package
