class EmptyQueueError(Exception):
    pass


class Queue:

    def __init__(self, default_size = 10):
        self.items = [None] * default_size
        self.front = 0
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty ")
        print(self.items)

    def insert_rear(self, x):

        if self.count == len(self.items):
            self.resize(2 * len(self.items))

        i = (self.front + self.count) % len(self.items)
        self.items[i] = x
        self.count += 1

    def insert_front(self, x):
        if self.count == len(self.items):
            self.resize(2 * len(self.items))


        self.front = (self.front -1) % len(self.items)
        self.items[self.front] = x
        self.count += 1

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("QUeue is empty.")

        deleted_item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return deleted_item

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty.")

        rear = (self.front + self.count - 1) % len(self.items)
        deleted_item = self.items[rear]
        self.items[rear] = None
        self.count -= 1
        return deleted_item

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty.")

        return self.items[self.front]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty.")

        rear = (self.front + self.count - 1) % len(self.items)
        return self.items[rear]

    def resize(self, new_size):
        old_list = self.items
        self.items = [None] * new_size
        i = self.front

        for j in range(self.count):
            self.items[j] = old_list[i]
            i = (i+1) % len(old_list)

        self.front = 0


#####################################################################

if __name__ == "__main__":
    qu = Queue(5)


    while True:
        print("1.Insert at front")
        print("2.Delete at rear")
        print("3.Display")
        print("4.First")
        print("5.Size")
        print("6.Insert at rear")
        print("7.Delete at front")
        print("8.Last")
        print("9.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = int(input("Enter the element to be inserted at front : "))
            qu.insert_front(x)

        elif choice == 2:
            x = qu.delete_rear()
            print(x, "element deleted from the queue")

        elif choice == 3:
            qu.display()

        elif choice == 4:
            print("Element at the front is: ", qu.first())

        elif choice == 5:
            print("Size of queue is: ",qu.size())

        elif choice == 6:
            x = int(input("Enter the element to be inserted at rear : "))
            qu.insert_rear(x)

        elif choice == 7:
            x = qu.delete_front()
            print(x, "element deleted from the queue")

        elif choice == 8:
            print("Element at the front is: ", qu.last())

        elif choice == 9:
            break

        else:
            print("Wrong choice")

        print()




