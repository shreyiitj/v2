nodes_meta_data = {0:{}, 1:{}, 2:{}}

class Node:

	def __init__(self, val):
		self.val = val
		self.next = None

	def add_neighbour(self, node):
		self.next = node

class LinkedList:
	head = None

	def add_node(self, node_index):
		head_copy = self.head
		if head_copy is None:
			head_copy = Node(node_index)
		else:
			while head_copy.next is not None:
				head_copy = head_copy.next
			head_copy.add_neighbour(Node(node_index))

class Graph:

	vertices = [] 			# list of linked lists

	def add_vertex(self, v):
		self.vertices.append(v)

	def add_edge(self, u, v):
		# u,v should be indexes / ids
		self.add_directed_edge(u,v)
		self.add_directed_edge(v,u)

	def add_directed_edge(self, u, v):
		ll = self.vertices[u]
		ll.add_node(v)







# need to create 4 LL
g = Graph()
for i in range(4):
	g.add_vertex(LinkedList())

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,0)

print(g)
for i in g.vertices:
	print(i)

