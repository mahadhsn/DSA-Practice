import heapq

# Initialize an empty priority queue
priority_queue = []

# Insert elements (priority, value)
heapq.heappush(priority_queue, (2, "Task 2"))  # Priority 2
heapq.heappush(priority_queue, (1, "Task 1"))  # Priority 1
heapq.heappush(priority_queue, (3, "Task 3"))  # Priority 3

# Remove and return the smallest priority element
highest_priority = heapq.heappop(priority_queue)
print(highest_priority)  # Output: (1, 'Task 1')

# View the current state of the queue
print(priority_queue)  # Output: [(2, 'Task 2'), (3, 'Task 3')]