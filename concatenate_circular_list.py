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

    def concatenate_list(self, list2):
        if self.last is None:
            self.last = list2.last
            return
        if list2.last is None:
            return

        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last


#################################################################################
list1 = CircularLinkedList()
list2 = CircularLinkedList()

print("enter first list")
list1.create_list()

print("enter second list")
list2.create_list()

print("first", list1.display_list())
print("second", list2.display_list())


list1.concatenate_list(list2)
list1.display_list()