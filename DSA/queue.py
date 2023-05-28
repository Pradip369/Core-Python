import sys

class Queue(object):

    def __init__(self):
        self.my_queue = []

    def enqueue(self,val):
        self.my_queue.append(val)
    
    def dequeue(self):
        if self.my_queue:
            self.my_queue.pop(0)
        else:
            print("Your queue is empty......")
    
    def show(self):
        print(self.my_queue)

    def exit(self):
        sys.exit()

qe = Queue()

while True:
    print("----------------------------------------------------")
    print(
        "Enqueue ---------- 1\n",
        "Dequeue ---------- 2 \n",
        "Show ---------- 3\n",
        "Exit ---------- 4\n"
    )
    n = int(input("Choose above option : "))

    if n == 1:
        ps_no = int(input("Enter number : "))
        qe.enqueue(ps_no)
    elif n == 2:
        qe.dequeue()
    elif n == 3:
        qe.show()
    elif n == 4:
        qe.exit()


# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i] > self.queue[max]:
					max = i
			item = self.queue[max]
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

if __name__ == '__main__':
	myQueue = PriorityQueue()
	myQueue.insert(12)
	myQueue.insert(1)
	myQueue.insert(14)
	myQueue.insert(7)
	print(myQueue)			
	while not myQueue.isEmpty():
		print(myQueue.delete())