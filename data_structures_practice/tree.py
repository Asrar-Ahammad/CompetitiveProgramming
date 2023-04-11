class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.parent = self
        self.children.append(child)
    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)


def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptop')
    cellphone = TreeNode('cellphone')
    tv = TreeNode('TV')

    root.add_child(laptop)
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Windows'))
    laptop.add_child(TreeNode('Linux'))

    root.add_child(cellphone)
    cellphone.add_child(TreeNode('samsung'))
    cellphone.add_child(TreeNode('Nokia'))
    cellphone.add_child(TreeNode('Pixel'))

    root.add_child(tv)
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass
