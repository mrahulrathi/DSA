class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self, default_size = 10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self,x):

        if self.count == len(self.items):
            self.resize(len(self.items) * 2)

        i = (self.front + self.count) % len(self.items)
        self.items[i] = x
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty. can't deque")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front+1) % len(self.items)
        self.count -= 1
        return x

    def display(self):
        print(self.items)

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty. can't peek")
        return self.items[self.front]

    def resize(self, new_size):
        old_list = self.items
        self.items = [None] * new_size
        i = self.front

        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1) % len(old_list)

        self.front = 0


##########################################################################################

if __name__ == "__main__":

    qu = Queue(5)

    while True:
        print("1.Enque")
        print("2.Dequeue")
        print("3.Display")
        print("4.Peek")
        print("5.Size")
        print("6.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = int(input("Enter the element to be enqueue : "))
            qu.enqueue(x)

        elif choice == 2:
            x = qu.dequeue()
            print(x, "element deleted from the queue")

        elif choice == 3:
            qu.display()

        elif choice == 4:
            print("Element at the front is: ", qu.peek())

        elif choice == 5:
            print("Size of queue is: ",qu.size())

        elif choice == 6:
            break

        else:
            print("Wrong choice")

        print()



