class Tree:
    def __init__(self, head=None, left=None, right=None):
        self.head = head
        self.left = left
        self.right = right


tree = Tree(
    'root',
    Tree(
        'a', 
        Tree(
            'ab',
            Tree(),
            Tree()
        ), 
        Tree(
            'ac',
            Tree(),
            Tree()
        )
    ),
    Tree(
        'b', 
        Tree(
            'ba',
            Tree(),
            Tree()
        ),
        Tree()
    )
)


print(tree.head)

print(tree.left.head)
print(tree.left.left.head)
print(tree.left.right.head)

print(tree.right.head)
print(tree.right.left.head)
