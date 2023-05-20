class StackEmptyError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):

        if self.is_empty():
            return 0

        count = 0
        p = self.top
        while p is not None:
            count +=1
            p = p.link

        return count

    def push(self, x):

        temp = Node(x)
        temp.link = self.top
        self.top = temp

    def pop(self):

        if self.is_empty():
            raise StackEmptyError("Stack is empty. Can't pop element")

        popped_element = self.top.info
        self.top = self.top.link
        return popped_element

    def peek(self):

        if self.is_empty():
            raise StackEmptyError("Stack is empty. Can't peek")

        return self.top.info

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        print("stack is : ")
        p = self.top
        while p is not None:
            print(p.info, " ", end="")
            p = p.link


####################################################################################################

if __name__ == "__main__":
    st = Stack()

    while True:
        print("1.Push")
        print("2.Pop")
        print("3.Display stack")
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



