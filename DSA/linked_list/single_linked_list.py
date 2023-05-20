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
        while i < k-1 and p is not None:
            i += 1
            p = p.link
        if p is None:
            print("you can only insert upto position ",i)
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
            print("Element ", x ," not found in list")
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

    def merge(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge(self.start, list2.start)
        return merge_list


    def _merge1(self,p1, p2):

        if p1.info <= p2.info:
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link

        # pM is newly inserted node in merge list
        pM = startM

        while p1 is not None or p2 is not None:
            if p1.info <= p2.info:
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

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
        if p1.info < p2.info:
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if p1.info < p2.info:
                pM.link = p1
                p1 = p1.link
            else:
                pM.link = p2
                p2 = p2.link
            pM = pM.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None

        slowR = self.start
        fastR = self.start
        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None


    def remove_cycle(self):
        c = self.find_cycle()
        if c is None:
            return None
        print("Node at which cycle was detected ", c.info)
        len_cycle = 0
        p = c
        q = c
        while True:
            len_cycle += 1
            q = q.link
            if p == q:
                break
        print("length of cycle is : ", len_cycle)
        len_rem_list = 0
        p = self.start
        while p != q:
            len_rem_list += 1
            p = p.link
            q = q.link

        print("Number of nodes not included in cycle are : ", len_rem_list)
        length_list = len_cycle + len_rem_list
        print("length of list is : ", length_list)
        for i in range(length_list-1):
            p = p.link

        p.link = None

    def insert_cycle(self, x):
        if self.start is None:
            return
        p = self.start
        prev = None
        px = None
        while p is not None:
            if p.info == x:
                 px = p
            prev = p
            p = p.link
        if px is not None:
            prev.link = px
        else:
            print(x, "element not found in list")


    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self, list_start):
        if list_start is None or list_start.link is None:
            return list_start

        start1 = list_start
        start2 = self._divide_list(list_start)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1, start2)
        return startM

    def _divide_list(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = p.link.link
        start2 = p.link
        p.link = None
        return start2

    def concatenate(self, list2):
        if self.start is None:
            self.start = list2.start
            return

        if list2.start is None:
            return
        p = self.start
        while p is not None:
            p = p.link
        p.link = list2.start



#####################################################################################################

list = SingleLinkedList()
list.create_list()

while True:
    print("1.Display List")
    print("2.Count the number of nodes")
    print("3.Search for an element")
    print("4.Insert in empty list/ Insert in beginning of list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.Merge sort")
    print("16.Insert cycle")
    print("17.Detect cycle")
    print("18.Remove sort")
    print("19.Quit")

    option = int(input("Enter your choice: "))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        list.insert_in_beginning(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element after which the data need to be inserted"))
        list.insert_after(data,x)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the element before which the data need to be inserted"))
        list.insert_before(data,x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the position at which the data need to be inserted"))
        list.insert_at_position(data, x)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        list.delete_node(x)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlinks()
    elif option == 15:
        list.merge_sort()
    elif option == 16:
        x = int(input("Enter the element at which the cycle has to be inserted : "))
        list.insert_cycle(x)
    elif option == 17:
        status = list.has_cycle()
        if status:
            print("list has cycle")
        else:
            print("list does not have cycle")
    elif option == 18:
        list.remove_cycle()
    elif option == 19:
        break
    else:
        print("Invalid input")
