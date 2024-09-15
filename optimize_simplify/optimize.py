import time
import random

# Function to implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements

# Generate a large list of random integers
array_size = 10000  # You can change the size as needed
random_list = [random.randint(0, 100000) for _ in range(array_size)]

# Track the time before the algorithm starts
start_time = time.time()

# Call the Bubble Sort function
bubble_sort(random_list)

# Track the time after the algorithm ends
end_time = time.time()

# Calculate and print the time taken
time_taken = end_time - start_time
print(f"Time taken by Bubble Sort: {time_taken:.5f} seconds")