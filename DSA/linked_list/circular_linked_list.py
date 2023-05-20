class Node(object):
    def __init__(self,value):
        self.info = value
        self.link = None

class CircularLinkedList(object):

    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last is None:
            print("list is empty")
            return

        p = self.last.link
        while True:
            print(p.info, " ", end="")
            p = p.link
            if p == self.last.link:
                break
        print()

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def create_list(self):

        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        data = int(input("Enter the element to be inserted "))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data = int(input("Enter the element to be inserted "))
            self.insert_at_end(data)

    def insert_after(self, data, x):

        p = self.last.link
        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break
        if p == self.last.link and p.info != x:
            print(x,"Element not found in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp

    def delete_first_node(self):
        # list is empty
        if self.last is None:
            return

        # list has only one node
        if self.last.link == self.last:
            self.last = None
            return

        self.last.link = self.last.link.link

    def delete_last_node(self):

        # list is empty
        if self.last is None:
            return

        # list has only one node
        if self.last.link == self.last:
            self.last = None
            return

        p = self.last.link
        while p.link != self.last:
            p = p.link

        p.link = self.last.link
        self.last = p

    def delete_node(self, x):
        # list is empty
        if self.last is None:
            return

        #list has only one node
        if self.last.link == self.last and self.last.info == x:
            self.last = None
            return

        #deletion of first node
        if self.last.link.info == x:
            self.last.link = self.last.link.link
            return

        p = self.last.link
        while p.link != self.last.link:
            if p.link.info == x:
                break
            p = p.link

        if p.link == self.last.link:
            print(x, "element not found in list")
            return
        else:
            p.link = p.link.link
            if x == self.last.info:
                self.last = p


#################################################################################
list = CircularLinkedList()
list.create_list()

while True:
    print("1.Display list")
    print("2.Insert in empty list")
    print("3.Insert a node at the beginning of the list")
    print("4.Insert a node at the end of the list")
    print("5.Insert a node after a specific node")
    print("6.Delete first node")
    print("7.Delete last node")
    print("8.Delete any node")
    print("9.Quit")

    option = int(input("Enter the choice : "))

    if option == 1:
        list.display_list()

    elif option == 2:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_empty_list(data)

    elif option == 3:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which to insert : "))
        list.insert_after(data, x)
    elif option == 6:
        list.delete_first_node()
    elif option == 7:
        list.delete_last_node()
    elif option == 8:
        data = int(input("Enter the Node to be deleted : "))
        list.delete_node(data)

    elif option == 9:
        break
    else:
        print("invalid input")





