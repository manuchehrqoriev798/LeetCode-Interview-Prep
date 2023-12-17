def find_level(root, target):
    if not root:
        return -1  # Return -1 if the tree is empty

    level = 0
    queue = [(root, level)]

    while queue:
        current_node, current_level = queue.pop(0)

        if current_node.val == target:
            return current_level

        if current_node.left:
            queue.append((current_node.left, current_level + 1))
        if current_node.right:
            queue.append((current_node.right, current_level + 1))

    return -1  # Return -1 if the target node is not found in the tree