class EmptyQueueError(Exception):
    pass


class queue:

    def __init__(self):
        self.items = []
        self.front = 0

    def is_empty(self):
        return len(self.items) == self.front

    def enqueue(self,x):
        self.items.append(x)

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty. can't deque")

        x = self.items[self.front]
        self.items[self.front] = None
        self.front += 1
        return x

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self.items)

    def size(self):
        return len(self.items) - self.front

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty. can't peek")
        return self.items[self.front]


##########################################################################################

if __name__ == "__main__":

    qu = queue()

    while True:
        print("1.Enque")
        print("2.Dequeue")
        print("3.Display Queue")
        print("4.diplay top element")
        print("5.Size")
        print("6.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = int(input("Enter the element to be enque : "))
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



