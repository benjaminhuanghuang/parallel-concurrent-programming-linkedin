# Data Race
The reason:
- two or more concurrent thread read/write same memory location
- At least one thread is modifying it


## Critical Section
- Code segment that access a shared resource
- Should be protected
- Need to be executed as an uniterupted action.
- ! Keep protected section as short as possible.

## Atomic Operation
- Execute as single action, uniterupt
