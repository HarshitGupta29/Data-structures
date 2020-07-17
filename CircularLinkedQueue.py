class CircularLinkedQueue:

    class _Node:
        slots = '_element','_next'
        def __init__(self,element,next):
            self._element=element
            self._next=next
    
    def __init__(self):
        self._tail=None
        self._size=0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._tail._next._element

    def is_empty(self):
        return self._size==0

    def enqueue(self,value):
        if self.is_empty():
            self._tail=self._Node(value,None)
            self._tail._next=self._tail
        else:
            new=self._Node(value,None)
            new._next=self._tail._next
            self._tail._next=new
            self._tail=new
        self._size+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer=self._tail._next._element
        self._tail._next=self._tail._next._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer