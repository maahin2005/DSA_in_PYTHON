# Queue

- A queue is a data structure that follows the First In, First Out (FIFO) principle.

- This means that the first element added to the queue is the first one to be removed.

- Think of it like a line of people: the first person in line is the first one to be served.

## Operations on a Queue

## Enqueue: Add an element to the end of the queue.

## Dequeue: Remove and return the front element of the queue.

## Front: Return the front element without removing it.

## isEmpty: Check if the queue is empty.

# Implementation of a Queue in Python

- You can use a list to implement a queue in Python, but it's more efficient to use collections.deque because it provides O(1) time complexity for appends and pops from both ends.
