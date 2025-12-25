class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    """Convert list to complete binary tree"""
    if not arr:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    
    for i in range(len(nodes)):
        if nodes[i] is None:
            continue
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        
        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]
    
    return nodes[0]

def visualize_tree(root):
    """ASCII art tree visualization"""
    def _get_tree_lines(root):
        if root is None:
            return [], 0, 0, 0
        
        # Get left and right subtree lines
        left_lines, left_pos, left_width, left_height = _get_tree_lines(root.left)
        right_lines, right_pos, right_width, right_height = _get_tree_lines(root.right)
        
        val_str = str(root.val)
        val_len = len(val_str)
        
        # Combine subtrees
        if left_height < right_height:
            left_lines += [' ' * left_width] * (right_height - left_height)
        elif right_height < left_height:
            right_lines += [' ' * right_width] * (left_height - right_height)
        
        # Create current node's representation
        lines = []
        first_line = ' ' * (left_pos + 1) + '_' * (left_width - left_pos - 1)
        first_line += val_str
        first_line += '_' * right_pos + ' ' * (right_width - right_pos)
        lines.append(first_line)
        
        # Add connection lines
        for i in range(max(len(left_lines), len(right_lines))):
            left_line = left_lines[i] if i < len(left_lines) else ' ' * left_width
            right_line = right_lines[i] if i < len(right_lines) else ' ' * right_width
            lines.append(left_line + ' ' * val_len + right_line)
        
        return lines, left_width + val_len // 2, left_width + val_len + right_width, len(lines)
    
    lines, _, _, _ = _get_tree_lines(root)
    return '\n'.join(lines)

# Example usage and demonstration
test_cases = [[50, 30, 45, 10, 15, 20, 40]

]

for i, arr in enumerate(test_cases, 1):
    print(f"\n=== Test Case {i} ===")
    print(f"Input list: {arr}")
    root = list_to_tree(arr)
    print("Tree visualization:")
    print(visualize_tree(root))
    print("-" * 40)



