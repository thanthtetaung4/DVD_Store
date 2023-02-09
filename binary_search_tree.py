from customer import Customer
from bstnode import BSTNode
from queue import Queue


class BST:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            iterator = self.root
            while iterator is not None:
                current = iterator
                if data < iterator.data:
                    iterator = iterator.left
                elif data > iterator.data:
                    iterator = iterator.right
                else:
                    return False
            new_node = BSTNode(data)
            if data < current.data:
                current.left = new_node
            else:
                current.right = new_node

    def is_leaf(self, data):
        root = self.root

        while root is not None:
            current = root
            if root.data == data:
                if root.left is None and root.right is None:
                    return True
                else:
                    return False
            elif data < root.data:
                root = root.left
            else:
                root = root.right

        return False

    def find_max(self, root):

        current = None
        while root is not self.is_leaf(root.data):
            current = root
            if self.is_leaf(current.data):
                return current.data
            root = root.right
        return root

    def find_mini(self, root):

        current = None
        while root is not self.is_leaf(root.data):
            current = root
            if self.is_leaf(current.data):
                return current.data
            root = root.left
        return root

    def get_node(self, data):
        root = self.root
        while root is not None:
            if data == root.data:
                return root
            elif data < root.data:
                root = root.left
            else:
                root = root.right
        return False

    def delete_node(self, node):
        # root = self.root
        # if root is None:
        #     return False
        # else:
        #     current = None
        #     while root is not None:
        #         current = root
        #         if node == current:
        pass

    def level_order_traverse(self):
        if self.root is None:
            return False

        q = Queue()
        q.enqueue(self.root)
        node = None
        result = []
        while not q.is_empty():
            node = q.dequeue()
            result.append(node)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return result

    def in_order_traverse(self, root, result):
        if not root:
            return
        self.in_order_traverse(root.left, result)
        result.append(root.data)
        self.in_order_traverse(root.right, result)
        ''' The reason why I use recursive is iterative will also cost Time => O(n) and Space => O(n)'''

    def __str__(self):
        output = ''
        node_list = []
        self.in_order_traverse(self.root, node_list)
        for item in node_list:
            output += str(item) + '\t'
        return output


if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(15)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(12)
    bst.insert(13)
    bst.insert(11)
    bst.insert(17)
    print('-' * 10)
    print('BST')
    print(bst.root.data)
    print(bst.root.left.data)
    print(bst.root.right.data)
    print(bst.root.left.data)
    print(bst.root.left.right.data)
    print(bst.root.left.right.right.data)
    print(bst.root.left.left.left.data)
    print(bst.root.right.left.right.data)
    print(bst.root.right.left.left.data)
    print(bst)
    dummy_list = bst.level_order_traverse()
    s = ''
    for i in dummy_list:
        s += str(i.data) + '\t'
    print(s)
    print(bst.is_leaf(17))
    node = bst.get_node(5)
    print(node.data)
    print(bst.find_max(node))
    print(bst.find_mini(node))
