## 3 challenges of producer-consumer
- Mutal exclusion on the queee of producter and consumer
- Prevent producer from trying to add data to full queue
- Prevent consumer from trying to remove data from an empty queue


## Solution
Use queue + mutation + condition variable
Python queue implemented all of the locks and synchronizaton mechanism
