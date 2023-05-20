class QueueEmptyError(Exception):
    pass


class Node:

    def __init__(self,value):
        self.info = value
        self.link = None


class Queue:

    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear == None

    def size(self):
        if self.is_empty():
            print("Queue is empty")
            return 0
        n = 0
        p = self.rear.link
        print("Queue is : ")
        while True:
            n += 1
            p = p.link
            if p == self.rear.link:
                break
        return n

    def enqueue(self, x):
        temp = Node(x)

        if self.is_empty():
            self.rear = temp
            self.rear.link = self.rear
        else:
            temp.link = self.rear.link
            self.rear.link = temp
            self.rear = temp

    def dequeue(self):

        if self.is_empty():
            raise QueueEmptyError("Queue is empty. element cannot be deleted")

        if self.rear == self.rear.link:
            deleted_element = self.rear
            self.rear = None
        else:
            deleted_element = self.rear.link
            self.rear.link = self.rear.link.link

        return deleted_element.info

    def peek(self):
        if self.is_empty():
            raise QueueEmptyError("Queue is empty. can't peek")
        return self.rear.link.info

    def display(self):

        if self.is_empty():
            print("queue is empty")
            return

        p = self.rear.link
        while True:
            print(p.info, " ", end="")
            p = p.link
            if p == self.rear.link:
                break

        print()



########################################################

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
            print("Size of queue is: ", qu.size())

        elif choice == 6:
            break

        else:
            print("Wrong choice")

        print()



