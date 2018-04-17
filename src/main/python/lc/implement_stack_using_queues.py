class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = collections.deque()
        
    def push(self, x): # O(1)
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        
    def pop(self): # O(N)
        """
        :rtype: nothing
        """
        return self.top_internal(False)

    def top(self): # O(N)
        """
        :rtype: int
        """
        return self.top_internal(True)
        
    def top_internal(self, keep):
        new_queue = collections.deque()
        cache = None
        while len(self.queue) != 0:
            top = self.queue.popleft()
            if cache is None:
                cache = top
            else:
                new_queue.append(cache)
                cache = top
                
        if keep:
            new_queue.append(cache)
        self.queue = new_queue
        return cache
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        
