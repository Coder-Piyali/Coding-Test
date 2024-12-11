# Write a Python program to convert a list of tuples into a dictionary.
tupleslist = [("a", 10), ("b", 20), ("c", 30), ("D", 40)] # Define a list of tuple

dictionary = dict(tupleslist) # Converting the list of tuples into a dictionary using the dict() function

print("The tuples and list converted Dictionary is:", dictionary) # Print the result

# Output: The tuples and list converted Dictionary is: {'a': 10, 'b': 20, 'c': 30, 'D': 40}

# print(type(dictionary)) # This line is for checking tuple and list is converted to dictionary or not
