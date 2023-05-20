class StackEmptyError(Exception):
    pass


class StackFullError(Exception):
    pass


class Stack:

    def __init__(self, max_size):

        self.items = [None] * max_size
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == len(self.items)

    def size(self):
        return self.count

    def push(self,x):

        if self.is_full():
            raise StackFullError("Stack is full. Can't push element")

        self.items[self.count] = x
        self.count += 1

    def pop(self):

        if self.is_empty():
            raise StackEmptyError("Stack is empty. Can't pop element")

        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -= 1
        return x

    def peek(self):

        if self.is_empty():
            raise StackEmptyError("Stack is empty. Can't peek")

        return self.items[self.count-1]

    def display(self):
        print(self.items)


####################################################################################################

if __name__ == "__main__":
    st = Stack(8)

    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Display list")
        print("4.diplay top element")
        print("5.Size")
        print("6.Quit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            x = int(input("Enter the element to be pushed in stack : "))
            st.push(x)

        elif choice == 2:
            x = st.pop()
            print(x, "element pop from the stack")

        elif choice == 3:
            st.display()

        elif choice == 4:
            print("Element at the top is: ", st.peek())

        elif choice == 5:
            print("Size of stack is: ",st.size())

        elif choice == 6:
            break

        else:
            print("Wrong choice")

        print()



