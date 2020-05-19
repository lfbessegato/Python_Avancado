import heapq

# https://docs.python.org/3.0/library/heapq.html

class PriorityQueue:
	def __init__(self):

		self._queue = []

		self._index = 0

	def push(self, item, priority):

		heapq.heappush(self._queue, (-priority, self._index, item))

		self._index += 1

	def pop(self):

		return heapq.heappop(self._queue)[-1]

class Person:
	def __init__(self, name):

		self.name = name

	def __repr__(self):

		return self.name

q = PriorityQueue()

q.push(Person('Marcos'), 28)

q.push(Person('Joao'), 30)

q.push(Person('Maria'), 15)

q.push(Person('Gabriel'), 40)

print(q.pop())