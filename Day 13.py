def counting_sort(arr):
  """
  Sorts an array of 0s, 1s, and 2s in ascending order using counting sort.

  Args:
    arr: The array to be sorted.

  Returns:
    A new array containing the sorted elements.
  """

  counts = [0, 0, 0]  # Create lists to store the counts of each element (like boxes for 0s, 1s, and 2s)
  for number in arr:  # Count how many of each number are in the array
    counts[number] += 1  # Put each number in its corresponding box

  sorted_arr = []  # Create an empty list to store the sorted numbers
  for i in range(3):  # Go through each box
    sorted_arr.extend([i] * counts[i])  # Take out the numbers from each box and put them in the sorted list

  return sorted_arr

# Get the array from the user
user_input = input("Enter the numbers in the array, separated by spaces: ")
arr = [int(number) for number in user_input.split()]  # Convert the input string into a list of numbers

# Sort the array using counting sort
sorted_arr = counting_sort(arr)

# Print the sorted array
print("The sorted array is:", sorted_arr)
