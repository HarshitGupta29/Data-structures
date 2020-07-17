class Stack:

    def __init__(self):
        self._data=[]

    def push(self,value):
        self._data.append(value)

    def pop(self):
        return(self._data.pop())
    
    def top(self):
        if len(self._data)==0 :
            return "error"
        else:
            return self._data[-1]
    
    def isEmpty(self):
        if len(self._data)==0 :
            return True
        else:
            return False

    def __len__(self):
        return len(self._data)

    def data(self):
        return self._data


s=Stack()
s.push(3)
s.push(9)
s.push(100)
print(s.isEmpty())
print(s.pop())
k=s.data()
l=len(s)
print(k,l)
s.pop()
s.pop()
l=len(s)
print(k,l)
print(s.top())
