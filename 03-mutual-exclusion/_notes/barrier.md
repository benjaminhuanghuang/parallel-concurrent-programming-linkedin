# Barrier
Barrier prevents a group of threads from proceeding until enough threads have reached the barrier

每个线程通过调用wait()尝试通过障碍，并阻塞，直到阻塞的数量达到parties时，阻塞的线程被同时全部释放。
action是一个可调用对象，当线程被释放时，其中一个线程会首先调用action，之后再跑自己的代码。
timeout时默认的超时时间。
