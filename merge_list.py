class Node:

    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info, " ", end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("Number of node in the list = ", n)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is at position : ", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, "Not found in list")
            return False

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):

        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of node : "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, "Not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):

        if self.start is None:
            print(x, "element not found in list")
            return
        if self.start.info == x:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        while p is not None:
            if p.link.info == x:
                break
            p = p.link
        if p is None:
            print(x, "not present in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        i = 1
        p = self.start
        while i < k - 1 and p is not None:
            i += 1
            p = p.link
        if p is None:
            print("you can only insert upto position ", i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info == x:
            self.start = self.start.link
            return
        p = self.start
        while p is not None:
            if p.link.info == x:
                break
            p = p.link
        if p is None:
            print("Element ", x, " not found in list")
        else:
            p.link == p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    """ 1) references are p, q, end => stop end when end refers to the second Node
        2) where end is None in the first pass p will be self.start and q = p.link, stop when end == p.link
     """

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    """Same as sort with data, with extra reference r which will be behind the p"""

    def bubble_sort_exlinks(self):
        end = None
        while self.start.link != end:
            r = p = self.start
            while p.link != end:
                q = p.link
                if q.info < p.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def merge1(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge1(self.start, list2.start)
        return merge_list

    def _merge1(self, p1, p2):

        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link;

        # pM is newly inserted node in merge list
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link;
            pM = pM.link;

        # If second list is finished and element left in 1st list
        if p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        # If first list is finished and element left in 2st list
        if p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge2(self.start, list2.start)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.info <= p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link = p1
                pM = pM.link
                p1 = p1.link
            else:
                pM.link = p2
                pM = pM.link
                p2 = p2.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

#####################################################################################################

list1 = SingleLinkedList()
list2 = SingleLinkedList()
list1.create_list()
list2.create_list()

list1.bubble_sort_exdata()
list2.bubble_sort_exdata()

print("first list - ", list1.display_list())
print("Second list - ", list2.display_list())

list3 = list1.merge1(list2)
print("merged list ", list3.display_list())
print("first list - ", list1.display_list())
print("Second list - ", list2.display_list())



list3 = list1.merge2(list2)
print("merged list - ", list3.display_list())
print("first list - ", list1.display_list())
print("Second list - ", list2.display_list())


