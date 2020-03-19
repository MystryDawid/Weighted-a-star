

class TreeNode:
    def __init__(self, val=None):
        self.value = val
        self.right = None
        self.left = None
        self.parent = None
        self.left_right = None  # 1 if right 0 if left

    def add_node(self, val):
        if self.value is None:
            self.value = TreeNode(val).value
        else:
            tmp = self
            while True:
                if tmp.value.h < val.h:
                    if tmp.right is None:
                        tmp.right = TreeNode(val)
                        tmp.right.parent = tmp
                        tmp.right.left_right = True
                        break
                    else:
                        tmp = tmp.right
                else:
                    if tmp.left is None:
                        tmp.left = TreeNode(val)
                        tmp.left.parent = tmp
                        tmp.left.left_right = False
                        break
                    else:
                        tmp = tmp.left

    def min_value_node(self, node=None):
        if node is None:
            node = self
        while node.left is not None:
            node = node.left
        return node

    def value_min_node(self, node=None):
        return self.min_value_node(node).value

    def max_value_node(self, node=None):
        if node is None:
            node = self
        while node.right is not None:
            node = node.right
        return node

    def value_max_node(self, node=None):
        return self.max_value_node(node).value

    def parent_node(self, node):
        if self.value == node.value:
            return None
        tmp = self
        while True:
            if tmp is not None:
                if tmp.value.h < node.value.h:
                    if tmp.right.value == node.value:
                        return tmp
                    else:
                        tmp = tmp.right
                        continue
                else:
                    if tmp.left.value == node.value:
                        return tmp
                    else:
                        tmp = tmp.left
                        continue
            else:
                return tmp

    def search(self, node):

        if self.value is not None:
            tmp = self
            while True:
                if tmp is not None:
                    if tmp.value is not None:

                        if tmp.value == node:
                            #print("jest")
                            return tmp
                        elif tmp.value.h >= node.h:
                            tmp = tmp.left
                            #print("left")
                            continue
                        else:
                            tmp = tmp.right
                            #print("right")
                            continue
                    else:
                        return None
                else:
                    return None

        else:
            return None

    def show(self):
        if self.value is not None:
            if self.left is not None:
                self.left.show()
            print("h:", self.value.h, self.value.position,  end=", ")
            if self.right is not None:
                self.right.show()
        else:
            print("None")

    def count(self):
        count = 1
        if self.left is not None:
            count += self.left.count()

        if self.right is not None:
            count += self.right.count()
        return count

    def del_note(self, val):
        node = self.search(val)

        if node is None:
            return None

        if node.right is not None:
            min_node = self.min_value_node(node.right)
        else:
            min_node = self.min_value_node(node)

        if min_node.parent is None:
            self.value = None
            return

        if node.value == min_node.value:
            if node.left_right:
                node.parent.right = None
            else:
                node.parent.left = None

        node.value = min_node.value

        if min_node.right is None and min_node.left is None:    # none child
            if min_node.left_right:
                min_node.parent.right = None
            else:
                min_node.parent.left = None

        if min_node.right is None != min_node.left is None:     # one child
            min_node.parent.right = min_node.right

