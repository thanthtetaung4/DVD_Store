
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def is_null(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def queue_size(self):
        return len(self.queue)
    def is_full(self):
        return False  # I don't need is full in my application

    def __str__(self):
        output = ''
        for q in self.queue:
            output += str(q) + '\t'
        return output

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.is_null())
    print(q.is_full())
    print(q)
    print(q.queue_size())
    q.dequeue()
    print(q.queue_size())
    print(q)
    print(q.peek())