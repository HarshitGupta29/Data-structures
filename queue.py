class Queue:
    Capacity=6
    def __init__(self):
        self._data=[None]*Queue.Capacity
        self._start=0
        self._size=0
    def enqueue(self,value):
        if len(self)!=self._size:
            self._data[(self._start+self._size)%Queue.Capacity]=value
        else:
            self.resize(2*Queue.Capacity)
            self._data[self._size%Queue.Capacity]=value
        self._size+=1
    def dequeue(self):
        if self.is_empty():
            return "error"
        temp,self._data[self._start]=self._data[self._start],None
        self._start=(self._start+1)%Queue.Capacity
        self._size-=1
        if self._size<Queue.Capacity//4:
            self.resize(Queue.Capacity//2)
        return temp
    def first(self):
        if self.is_empty():
            return "error"
        return (self._data[self._start])  
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return self._size==0
    def resize(self,cap):
        old=self._data
        self._data=[None]*cap
        for i in range(self._size):
            self._data[i]=old[self._start%Queue.Capacity]
            self._start+=1
        self._start=0
        Queue.Capacity=cap
    def return_list(self):
        return self._data

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.dequeue()

q.dequeue()
q.dequeue()
q.dequeue()

q.dequeue()
print(q.return_list())