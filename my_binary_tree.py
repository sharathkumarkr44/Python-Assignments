from binary_tree import BinaryTree


class MyBinaryTree(BinaryTree):
    def height(self) -> int:
        """Returns the height of this tree."""
        def _height_helper(node):
            if node is None:
                return 0
            left_height = _height_helper(node._left)
            right_height = _height_helper(node._right)
            return max(left_height, right_height) + 1
        return _height_helper(self)

    def max_sum(self) -> int:
        """Returns the maximum sum of the left and right sub-tree."""
        left_node = self.get_left()
        q = [left_node]
        left_node_sum = 0
        if left_node is not None:
            while len(q) > 0:
                node = q[0]
                q.pop(0)
                if node._left is not None:
                    q.append(node._left)
                if node._right is not None:
                    q.append(node._right)
                left_node_sum += node._item

        right_node = self.get_right()
        right_node_sum = 0
        q = [right_node]
        right_node_sum = 0
        if right_node is not None:
            while len(q) > 0:
                node = q[0]
                q.pop(0)
                if node._left is not None:
                    q.append(node._left)
                if node._right is not None:
                    q.append(node._right)
                right_node_sum += node._item

        return max(left_node_sum, right_node_sum)

    def max_path(self) -> int:
        self.max_path_result = self.get_root()._item

        def maxpath(node):
            if not node:
                return 0
            x = node._item
            l = maxpath(node._left)
            r = maxpath(node._right)
            self.max_path_result = max(self.max_path_result, x+l+r)
            return max(x+l, x+r)
        result = maxpath(self.get_root())
        return result

    def max_width(self) -> int:
        maxWidth = 0
        nodesInLevel = 0
        queue = []
        if (self.get_root()._item == None):
            return 0
        else:
            queue.append(self.get_root())

            while (len(queue) != 0):
                nodesInLevel = len(queue)
                maxWidth = max(maxWidth, nodesInLevel)
                while (nodesInLevel > 0):
                    current = queue.pop(0)
                    if (current.get_left() != None):
                        queue.append(current._left)
                    if (current.get_right() != None):
                        queue.append(current._right)
                    nodesInLevel = nodesInLevel - 1
        return maxWidth


if __name__ == "__main__":
    r3_tree = MyBinaryTree(item=88)
    r2_tree = MyBinaryTree(item=21, right=r3_tree)
    l2_tree = MyBinaryTree(item=58, left=r2_tree)
    # l_tree = MyBinaryTree(item=89, left=l2_tree, right=r2_tree)
    # r_tree = MyBinaryTree(item=48)
    tree = MyBinaryTree(item=0, right=l2_tree)

    # l2_tree = MyBinaryTree(item=5)
    # r2_tree = MyBinaryTree(item=7)
    # l3_tree = MyBinaryTree(item=4, left=l1_tree, right=r1_tree)
    # r3_tree = MyBinaryTree(item=1, left=l2_tree, right=r2_tree)
    # tree = MyBinaryTree(item=-8, left=l3_tree, right=r3_tree)
    print(tree.max_sum())
