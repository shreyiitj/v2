import random

class Heap:

	def __init__(self):
		self.arr = []
		self.last = None 		# index of last element.
		self.empty_heap_message = "heap is empty"

	def insert(self, v):
		self.check_heap_size()
		if self.last is None:
			self.last = 0
		else:
			self.last += 1
		self.arr[self.last] = v
		self.heapify_up()

	def extract_min(self):
		if self.last:
			min_elem = self.arr[0]
			self.arr[0] = self.arr[self.last]
			self.last -= 1
			self.heapify_down()
			return min_elem
		else:
			return self.empty_heap_message

	def check_heap_size(self):
		if not self.last or len(self.arr) <= self.last+1:
			self.arr.append(None)

	def swap(self, index1, index2):
		temp = self.arr[index1]
		self.arr[index1] = self.arr[index2]
		self.arr[index2] = temp

	def get_parent_index(self, index):
		if index % 2 == 0:
			return int((index-2)/2)
		else:
			return int((index-1)/2)

	def heapify_up(self):
		self._heapify_up(self.last)

	def _heapify_up(self, index):
		parent_index = self.get_parent_index(index)
		if parent_index >= 0 and self.arr[parent_index] > self.arr[index]:
			self.swap(index, parent_index)
			self._heapify_up(parent_index)

	def heapify_down(self):
		self._heapify_down(0)

	def _heapify_down(self, index):
		c1_index = 2*index + 1
		c2_index = 2*index + 2
		if not c1_index > self.last:
			c1_val = self.arr[c1_index]
			c2_val = None
			if c2_index <= self.last:
				c2_val = self.arr[c2_index]
			min_val_index = c1_index
			if c2_val and c2_val < c1_val:
				min_val_index = c2_index

			if self.arr[index] > self.arr[min_val_index]:
				self.swap(index, min_val_index)
				self._heapify_down(min_val_index)


h = Heap()
for i in range(10):
	x = random.randint(1,1000)
	print(x)
	h.insert(x)

print(h.arr)
