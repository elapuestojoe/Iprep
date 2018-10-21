class Queue(object):

    def __init__(self):
        self.queue = []
    
    def enqueue(self, object):
        self.queue.insert(0, object)

    def dequeue(self):
        if(self.isEmpty()):
            return self.queue.pop()
        else:
            return False
            
    def isEmpty(self):
        return len(self.queue) == 0