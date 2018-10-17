
def lowest_common_ancestor_BT(binary_tree, node_a, node_b):
    if binary_tree is None or node_a is None or node_b is None:
        return None

    if node_a is binary_tree or node_b is binary_tree:
        return binary_tree

    count_a = 0
    count_b = 0

    hold_a = node_a
    while hold_a is not binary_tree:
        count_a += 1
        #print("finding parent of : " + str(hold_a.data))
        hold_a = parent(binary_tree, hold_a)

    hold_b = node_b
    while hold_b is not binary_tree:
        count_b += 1
        #print("finding parent of : " + str(hold_b.data))
        hold_b = parent(binary_tree, hold_b)

    if count_a > count_b:
        hold_a = node_a
        for i in range (0, count_a-count_b):
            #print("finding parent of : " + str(hold_a.data))
            hold_a = parent(binary_tree, hold_a)
    else:
        hold_b = node_b
        for i in range(0, count_b-count_a):
            #print("finding parent of : " + str(hold_b.data))
            hold_b = parent(binary_tree, hold_b)

    while hold_a.data is not hold_b.data:
        hold_a = parent(binary_tree, hold_a)
        hold_b = parent(binary_tree, hold_b)

    return hold_a


def parent(root, node):
    if root is None or node is None or root.data is node.data:
        return root

    else:

        if root.left is not None and root.left.data is node.data:
            return root
        elif root.right is not None and root.right.data is node.data:
            return root

        else:
            if root.data < node.data:
                return parent(root.right, node)
            else:
                return parent(root.left, node)
