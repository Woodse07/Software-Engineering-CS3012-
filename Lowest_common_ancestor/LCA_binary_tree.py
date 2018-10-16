
def lowest_common_ancestor_BT(binary_tree, node_a, node_b):
    count_a = 0
    count_b = 0

    hold_a = node_a
    while hold_a is not None:
        count_a += 1
        hold_a = parent(binary_tree, hold_a)

    hold_b = node_b
    while hold_b is not None:
        count_b += 1
        hold_b = parent(binary_tree, hold_b)

    if count_a > count_b:
        hold_a = node_a
        for i in range (0, countA-countB):
            hold_a = parent(binary_tree, hold_a)
    else
        hold_b = node_b
        for i in range(0, countB-countA):
            hold_b = parent(binary_tree, hold_b)

    while hold_a != hold_b:
        hold_a = parent(binary_tree, hold_a)
        hold_b = parent(binary_tree, hold_b)


def parent(root, node):
    if(root.data == node.data):
        return None
    else:
        if root.left.data == node.data or root.right.data == node.data:
            return root
    else:
        if root.data < node.data:
            return parent(root.right, node)
        else
            return parent(root.left, node)
