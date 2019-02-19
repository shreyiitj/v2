class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Bst:

	def __init__(self):
		self.root = None

	def add_node(self, v):
		if not self.root:
			self.root = TreeNode(v)
		else:
			self._add_node(self.root, v)

	def _add_node(self,root,v): 			# supposed to be called from internal functions.
		if v > root.val:
			if root.right is None:
				root.right = TreeNode(v)
			else:
				self._add_node(root.right, v)
		elif v < root.val:
			if root.left is None:
				root.left = TreeNode(v)
			else:
				self._add_node(root.left, v)
		else:
			print("Value already present in tree")

	def traverse(self):
		if self.root:
			self._traverse(self.root)

	def _traverse(self, curr):
		if curr:
			self._traverse(curr.left)
			print(curr.val)
			self._traverse(curr.right)


def fill_tree(tree):
	from random import randint
	for i in range(100):
		tree.add_node(randint(0,100))

	return tree

tree = Bst()
tree = fill_tree(tree)
tree.traverse()
