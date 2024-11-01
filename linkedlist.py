class Node:
    def _init_(self, data):  
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


n = int(input())


linked_list = LinkedList()

for _ in range(n):
    data = int(input())
    linked_list.append(data)
print()
linked_list.printLinkedList()
