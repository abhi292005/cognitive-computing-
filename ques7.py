#7.1
file_name = 'example.txt'

# 
with open(file_name, 'w') as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This file is created for demonstration purposes.")

# 
with open(file_name, 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)

    #7.2
with open(file_name, 'a') as file:
    file.write("\nThis line is appended to the file.")


with open(file_name, 'r') as file:
    updated_content = file.read()
    print("Updated content of the file:")
    print(updated_content)

    #7.3
    
with open(file_name, 'r') as file:
    lines = file.readlines()
    line_count = len(lines)

print(f"The number of lines in the file is: {line_count}")