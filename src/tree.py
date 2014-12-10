class TreeNode(object):

    def __init__(self, value, children):
        super(TreeNode, self).__init__()
        self.value = value
        self.children = children


class BinaryTreeNode(object):

    def __init__(self, value, left, right):
        super(BinaryTreeNode, self).__init__()
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        res = "{!s} l:({!r} r:({!r})".format(self.value, self.left, self.right)
        return res


def random_binary_tree(depth, variance=3, node_value=0):
    import random
    if depth <= 0:
        node = None
        node_under = 0
    else:
        left, node_left = random_binary_tree(depth + random.randrange(-variance, 0),
                                             variance,
                                             node_value + 1)
        right, node_right = random_binary_tree(depth + random.randrange(-variance, 0),
                                               variance,
                                               node_value + 1 + node_left)
        node = BinaryTreeNode(node_value, left, right)
        node_under = node_left + node_right + 1
    return node, node_under


if __name__ == '__main__':
    print random_binary_tree(5)
