# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    left_max_node = root.value
    right_max_node = root.value

    if root.left_child is not None:
        if left_max_node < root.value:
            left_max_node = root.value
        left_max_node = greatest_node(root.left_child)

    if root.right_child is not None:
        if right_max_node < root.value:
            right_max_node = root.value
        right_max_node = greatest_node(root.right_child)

    return max(left_max_node, right_max_node)

if __name__ == "__main__":
    tree = Node(3)

    tree.left_child = Node(5)
    tree.left_child.left_child = Node(7)
    tree.left_child.right_child = Node(10)
    tree.left_child.right_child.left_child = Node(3)
    tree.left_child.right_child.right_child = Node(13)

    tree.right_child = Node(6)
    tree.right_child.right_child = Node(11)
    
    print(greatest_node(tree))
