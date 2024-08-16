class Queue:
    def __init__(self):
        self._queue = []
    
    def enqueue(self,item):
        self._queue.append(item)
    
    def dequeue(self):
        if len(self._queue):
            popEl = self._queue.pop(0)
            print(popEl)
    def front(self):
        if len(self._queue):
            print(self._queue[0])
    def isEmpty(self):
        print(len(self._queue)==0)
    def size(self):
        print(len(self._queue))
    def get(self):
        print(self._queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(7)
queue.dequeue()
queue.isEmpty()
queue.get()
queue.front()
queue.size()


