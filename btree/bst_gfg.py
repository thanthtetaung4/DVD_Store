"""Python3 program to demonstrate insert
operation in binary search tree """


# A Binary Tree Node
# Utility function to create a
# new tree node


class newNode:

    # Constructor to create a newNode
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = self.parent = None


# A utility function to insert a new
# Node with given key in BST


def insert(root, key):
    # Create a new Node containing
    # the new element
    newnode = newNode(key)

    # Pointer to start traversing from root
    # and traverses downward path to search
    # where the new node to be inserted
    x = root

    # Pointer y maintains the trailing
    # pointer of x
    y = None

    while (x != None):
        y = x
        print(y.key)
        if (key < x.key):
            x = x.left
            print(x)
        else:
            x = x.right

    # If the root is None i.e the tree is
    # empty. The new node is the root node
    if (y == None):
        y = newnode

    # If the new key is less than the leaf node key
    # Assign the new node to be its left child
    elif (key < y.key):
        y.left = newnode

    # else assign the new node its
    # right child
    else:
        y.right = newnode

    # Returns the pointer where the
    # new node is inserted
    return y


# A utility function to do inorder
# traversal of BST


def Inorder(root):
    if (root == None):
        return
    else:
        Inorder(root.left)
        print(root.key, end=" ")
        Inorder(root.right)


# Driver Code
if __name__ == '__main__':
    """ Let us create following BST
			50
		/ \
		30	 70
		/ \ / \
	20 40 60 80 """

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Pr inorder traversal of the BST
    Inorder(root)

# This code is contributed by
# SHUBHAMSINGH10
