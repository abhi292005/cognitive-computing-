#5.1
numbers = [1, 5, 2, 8, 3]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

print("Largest number:", largest)
print("Smallest number:", smallest)



#5.2
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

key_to_find = "age"

if key_to_find in my_dict:
    value = my_dict[key_to_find]
    print(f"The value for key '{key_to_find}' is: {value}")
else:
    print(f"Key '{key_to_find}' not found in the dictionary.")



#5.3
    numbers = [5, 2, 8, 1, 3]

# Ascending order
numbers.sort()
print("Ascending order:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)



#5.4
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print("Merged dictionary:", merged_dict)