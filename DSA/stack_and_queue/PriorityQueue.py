class Node:
    def __init__(self, data, priority):
        self.info = data
        self.priority = priority
        self.link = None


class EmptyQueueError(Exception):
    pass


class PriorityQueue:

    def __init__(self):
        self.front = None

    def enqueue(self, data, data_priority):
        temp = Node(data, data_priority)

        # if queue is empty or the element has priority more than first element
        if self.is_empty() or data_priority < self.front.priority:
            temp.link = self.front
            self.front = temp

        else:
            p = self.front
            while p.link != None and p.link.priority <= data_priority:
                p = p.link

            temp.link = p.link
            p.link = temp

    def dequeue(self):

        if self.is_empty():
            raise EmptyQueueError

        x = self.front.info
        self.front = self.front.link
        return x

    def is_empty(self):
        return self.front == None

    def display(self):

        if self.is_empty():
            print("Queue is empty")
            return

        p = self.front
        print("Queue is : ")
        while p != None:
            print(p.info, "       ", p.priority)
            p = p.link
        print()

    def size(self):
        n = 0
        p = self.front
        while p != None:
            p = p.link
            n += 1
        return n

####################################################################################################


if __name__ == "__main__":
    qu = PriorityQueue()

    while True:

        print("1.Display")
        print("2.Enqueue")
        print("3.Dequeue")
        print("4.Size")
        print("5.Quit")

        choice = int(input("Enter the choice : "))
        if choice == 1:
            qu.display()

        elif choice == 2:
            x = int(input("Enter the element to be added : "))
            data_priority = int(input("Enter the priority of the element : "))
            qu.enqueue(x, data_priority)

        elif choice == 3:
            x = qu.dequeue()
            print("Element is : ", x)

        elif choice == 4:
            print("Size of queue is : ", qu.size())

        elif choice == 5:
            break

        else:
            print("Wrong choice")

        print()


