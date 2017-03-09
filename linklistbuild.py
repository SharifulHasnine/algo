from Linklist.Node import Node

class linklist(object):
    def __init__(self):
        self.head = None;
        self.count = 0

    def insertFirst(self,data):
        self.count += 1
        self.data = data
        newNode = Node(data);
        if self.head is None:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head =newNode;
    def travarse(self):
        actualnode = self.head
        while actualnode is not None:
            print(actualnode.data)
            actualnode = actualnode.nextNode
    def size(self):
        return self.count;

    def insertLast(self,data):
        self.count += 1
        newNode = Node(data);
        if self.head is None:
            self.insertFirst(data)
            return


        actual = self.head


        while actual.nextNode is not None:
            actual =actual.nextNode
        actual.nextNode=newNode

    def remove(self, data):
        actual = self.head
        if self.head:
            if data == self.data:

                self.head = actual.nextNode

            else :
                return actual.remove(data, self.head)
                #print(self.head + " is removed")

    def reverse(self):
        prev = None
        actual = self.head
        while actual:
            next = actual.nextNode
            actual.nextNode = prev
            prev = actual
            actual = prev

            print("ffdf")
        self.head = prev










