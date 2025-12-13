# import time

# start_time = time.time()

# for i in range(0, 10):
#     print(i)

# print(time.time() - start_time)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
node1 = Node(2)
node2 = Node(8)
node3 = Node(9)
node4 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")
















# Display schedule

# Book a seat

# Cancel booking

# Show remaining seats

# Store booking history