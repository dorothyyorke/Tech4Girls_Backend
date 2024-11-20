# Question 3: Dictionary Lookup
data = {"name": "Alice", "age": 25, "country": "Wonderland"}
key = input("Enter the key you want to look up: ")
try:
    print("Value:", data[key])
except KeyError:
    print(f"Error: The key '{key}' does not exist in the dictionary.")