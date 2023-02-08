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
