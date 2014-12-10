from tree import BinaryTreeNode, random_binary_tree


def pre_order_traversal(node, callback):
    assert isinstance(node, BinaryTreeNode)
    assert hasattr(callback, '__call__')
    # root
    callback(node)
    # left
    if node.left is not None:
        pre_order_traversal(node.left, callback)
    # right
    if node.right is not None:
        pre_order_traversal(node.right, callback)


def in_order_traversal(node, callback):
    assert isinstance(node, BinaryTreeNode)
    assert hasattr(callback, '__call__')
    # left
    if node.left is not None:
        in_order_traversal(node.left, callback)
    # root
    callback(node)
    # right
    if node.right is not None:
        in_order_traversal(node.right, callback)


def post_order_traversal(node, callback):
    assert isinstance(node, BinaryTreeNode)
    assert hasattr(callback, '__call__')
    # left
    if node.left is not None:
        post_order_traversal(node.left, callback)
    # right
    if node.right is not None:
        post_order_traversal(node.right, callback)
    # root
    callback(node)


def main():
    def print_callback(n):
        print n.value,

    tree_top_node, _ = random_binary_tree(10)
    print tree_top_node

    print "\npre_order_traversal"
    pre_order_traversal(tree_top_node, print_callback)

    print "\nin_order_traversal"
    in_order_traversal(tree_top_node, print_callback)

    print "\npost_order_traversal"
    post_order_traversal(tree_top_node, print_callback)


if __name__ == "__main__":
    main()