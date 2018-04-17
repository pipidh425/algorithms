class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.pusher = []
        self.popper = []
        
        
    def push(self, x): # O(1)
        """
        :type x: int
        :rtype: nothing
        """
        self.pusher.append(x)


    def pop(self): # O(N)
        """
        :rtype: nothing
        """
        if len(self.popper) > 0:
            self.popper.pop()
        else:
            while len(self.pusher) > 0:
                self.popper.append(self.pusher.pop())
            if len(self.popper) > 0:
                self.popper.pop()
        
    

    def peek(self): # O(N)
        """
        :rtype: int
        """
        if len(self.popper) > 0:
            return self.popper[-1]
        while len(self.pusher) > 0:
            self.popper.append(self.pusher.pop())
        if len(self.popper) > 0:
            return self.popper[-1]
        return None
        

    def empty(self): # O(1)
        """
        :rtype: bool
        """
        return len(self.pusher) == 0 and len(self.popper) == 0
