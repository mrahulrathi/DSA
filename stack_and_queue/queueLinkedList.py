class QueueEmptyError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_size = 0

    def is_empty(self):
        return self.front == None

    def size(self):
        return self.queue_size

    def enqueue(self, x):
        temp = Node(x)
        if self.front is None:
            self.front = temp
        else:
            self.rear.link = temp

        self.rear = temp
        self.queue_size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty")

        x = self.front.info
        self.front = self.front.link
        self.queue_size -= 1
        return x

    def peek(self):

        if self.is_empty():
            raise QueueEmptyError("Queue is empty. Can't peek")

        return self.front.info

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue is : ")
        p = self.front
        while p is not None:
            print(p.info, " ", end="")
            p = p.link
        print()

####################################################################################################

if __name__ == "__main__":
    qu = Queue()

    while True:
        print("1.Enqueue")
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
            print("Element at the front end is: ", qu.peek())

        elif choice == 5:
            print("Size of queue is: ",qu.size())

        elif choice == 6:
            break

        else:
            print("Wrong choice")

        print()



