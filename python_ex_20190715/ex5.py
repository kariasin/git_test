from abc import *

class AbstrctQueue(metaclass=ABCMeta):
    @abstractmethod
    def enqueue(self, data):
        raise NotImplemented
    
    @abstractmethod
    def dequeue(self):
       raise NotImplemented

import queue
class QueueSet(AbstrctQueue):
    def __init__(self, type):
        if type == '1':
            self.data_queue = queue.Queue()
        elif type == '2':
            self.data_queue = queue.PriorityQueue()
        else:
            self.data_queue = queue.LifoQueue()

    def enqueue(self,data):
        self.data_queue.put(data)
    
    def dequeue(self):
        return self.data_queue.get()

fifo_queue = QueueSet(1)
for num in range(10):
    fifo_queue.enqueue(num)

for index in range(10):
    print(fifo_queue.dequeue())

lilo_queue = QueueSet(2)
for num in range(10):
    lilo_queue.enqueue(num)

for index in range(10):
    print(lilo_queue.dequeue())

priority_queue = QueueSet(3)
for num in range(10):
    priority_queue.enqueue((1,num))

for index in range(10):
    print(priority_queue.dequeue())