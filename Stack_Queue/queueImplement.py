from collections import deque

q = deque()

# Enqueue Operation
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

# Dequeue Operation
q.popleft()

# Front Operation
print("Front Operation: ", q[0])

print(q)