class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)

    def print_leaf_nodes(self, node=None):
        if node is None:
            node = self.root

        if node.right is None and node.left is None:
            print(node.key)

        if node.right:
            self.print_leaf_nodes(node.right)
        if node.left:
            self.print_leaf_nodes(node.left)

b = BST()


b.insert(8)
b.insert(3)
b.insert(10)
b.insert(14)
b.insert(1)
b.insert(6)
b.insert(9)
# b.insert(10)
# b.insert(11)
# b.insert(12)
b.print_leaf_nodes()

