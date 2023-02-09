from customer import Customer


class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

if __name__ == '__main__':
    node = BSTNode(1)
    node_2 = BSTNode(2)
    node_3 = BSTNode(3)
    node.left = node_2
    node.right = node_3
    if node.left and node.right:
        print(1)
