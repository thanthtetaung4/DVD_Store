class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def traverse(self, root, result):
        if root is None:
            return
        result.append(root)
        self.traverse(root.left, result)
        self.traverse(root.right, result)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def __str__(self):
        output = ''
        items = []
        self.traverse(self.root, items)
        n = 0
        count = 0
        for item in items:
            output += str(item.value) + '\t'
            count += 1
            if count == 2 ** n:
                count = 0
                output +='\n'
                n+=1
        return output


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(11)
    bst.insert(6)

    print(bst)
