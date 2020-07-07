

main thread is finished executing and there aren't any 
non-daemon threads left running, this process can terminate.
 

 detached thread was terminated abruptly with the process, it didn't have a chance to gracefully shutdown and stop what I was doing. That's fine, in the case of a garbage collection routine because all of the memory this process was using will get cleared as part of terminating it. 
 
 But if detached thread was doing some sort of io operation like writing to a file, then terminating in the middle of that operation could end up corrupting data. If you detach a thread to make it a background task, make sure it won't have any negative side effects if it prematurely exits. 