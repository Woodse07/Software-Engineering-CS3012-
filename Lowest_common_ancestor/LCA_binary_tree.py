import binary_tree as BT
def lowest_common_ancestor_BT(binary_tree, node_a, node_b):
    flag=0
    if binary_tree is None or node_a is None or node_b is None:
        return None
    if(not isinstance(binary_tree, BT.Node) or not isinstance(node_a, BT.Node) or not isinstance(node_b, BT.Node)):
        return None
    if binary_tree.data is None or node_a.data is None or node_b.data is None:
        return None
    if node_a.data is node_b.data:
        return node_a
    if binary_tree.data is node_a.data or binary_tree.data is node_b.data:
        return binary_tree


    if node_a.data == binary_tree.data or node_b.data == binary_tree.data:
        flag=1

    left_subtree = lowest_common_ancestor_BT(binary_tree.left, node_a, node_b)
    right_subtree = lowest_common_ancestor_BT(binary_tree.right, node_a, node_b)

    if left_subtree is None and right_subtree is None:
        if flag==0:
            return None
        else:
            return binary_tree

    if left_subtree is not None and right_subtree is not None:
        return binary_tree

    if left_subtree is None:
        if flag==1:
            if (right_subtree.data!=node_a and right_subtree.data!=node_b) or right_subtree.data==binary_tree.data:
                return right_subtree
            elif right_subtree.data!=binary_tree.data:
                return binary_tree
        else:
            return right_subtree
    else:
        if flag==1:
            if (left_subtree.data!=p and left_subtree.data!=node_b) or left_subtree.data==binary_tree.data:
                return left_subtree
            elif left_subtree.data!=binary_tree.data:
                return binary_tree
        else:
            return left_subtree
