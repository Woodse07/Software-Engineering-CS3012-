from LCA_binary_tree import parent
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def printTree(self):
        print("("),
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()
        print(")"),


BT = Node(10)
BT.insert(5)
BT.insert(15)
BT.insert(2)
BT.insert(1)
print(parent(BT, BT.left.left).data)
print(parent(BT, BT.left.left.left).data)
