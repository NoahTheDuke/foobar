class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BinarySearchTree:
    def __init__(self, root=None):
        if root:
            self.root = Node(root)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if value <= node.value:
            if node.left:
                self.insert_node(node.left, value)
            else:
                node.left = Node(value)
        elif value > node.value:
            if node.right:
                self.insert_node(node.right, value)
            else:
                node.right = Node(value)

    def count(self):
        return self.count_nodes(self.root)

    def count_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        elif node.left is None:
            return 1 + self.count_nodes(node.right)
        elif node.right is None:
            return 1 + self.count_nodes(node.left)
        else:
            total = 1
            total += self.count_nodes(node.left)
            total += self.count_nodes(node.right)
            return total

    #see: http://btv.melezinek.cz/pseudocodes.html
    def in_order_print(self, root=None):
        if not root:
            root = self.root
        left_values = self.in_order_print(root.left) if root.left else []
        right_values = self.in_order_print(root.right) if root.right else []
        return left_values + [root.value] + right_values

    def pre_order_print(self, root=None):
        if not root:
            root = self.root
        left_values = self.pre_order_print(root.left) if root.left else []
        right_values = self.pre_order_print(root.right) if root.right else []
        return [root.value] + left_values + right_values

    def post_order_print(self, root=None):
        if not root:
            root = self.root
        left_values = self.post_order_print(root.left) if root.left else []
        right_values = self.post_order_print(root.right) if root.right else []
        return left_values + right_values + [root.value]

def answer(seq):
    first, rest = seq[0], seq[1:]
    bst = BinarySearchTree(first)
    for i in rest:
        bst.insert(i)
    result = count_orderings(bst, bst.root)
    return str(result)

#see: http://stackoverflow.com/questions/17119116/how-many-ways-can-you-insert-a-series-of-values-into-a-bst-to-form-a-specific-tr
def count_orderings(bst, node):
    if node is None:
        return 1
    else:
        m = bst.count_nodes(node.left)
        n = bst.count_nodes(node.right)
        return choose(m + n, n) * count_orderings(bst, node.left) * count_orderings(bst, node.right)

choose_memo = {}

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if (n, k) in choose_memo:
        return choose_memo[(n, k)]

    m = n
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        result =  long(ntok // ktok)
    else:
        result = 0

    choose_memo[(m, k)] = result

    return result

test = [5, 9, 8, 2, 1]
test_ans = "6"
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_ans = "1"
test = [4, 2, 1, 3, 6, 5, 7]
test_ans = "80"
#test = [24, 14, 27, 7, 18, 26, 51, 6, 10, 20, 67, 11]
#test_ans = "1"
#test = [72, 53, 80, 35, 60, 78, 25, 37, 58, 64, 14, 28, 65]
#test_ans = "1"
ans = answer(test)
print(ans)
print(ans == test_ans)
