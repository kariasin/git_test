from abc import *

class AbstractQueue(metaclass=ABCMeta):
    @abstractmethod
    def enqueue(self, data):        #데이터의 추가
        raise NotImplemented

    @abstractmethod
    def dequeue(self):              #데이터 꺼내오기
        raise NotImplemented 

class DaveQueue(AbstractQueue):
    def __init__(self):
        self.items = list()

    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        data = self.items[0]
        del self.items[0]
        return data
dave_queue = DaveQueue()
for num in range(10):
    dave_queue.enqueue(num)
print(dave_queue.dequeue())    