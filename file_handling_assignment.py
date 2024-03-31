# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with some numbers: 987\n")
except IOError as e:
    print("Error:", e)
finally:
    print("File creation completed.")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("Error: File not found.")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Additional line 1.\n")
        file.write("Appending some more text.\n")
        file.write("Last line.\n")
except PermissionError as e:
    print("Error:", e)
finally:
    print("File appending completed.")