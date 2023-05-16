import os

def read_file(filename):
    file = open(filename, 'r')
    content = file.read()
    print(content)
    file.close()

def write_file(filename):
    file = open(filename, 'w')
    data = input("Enter data to write to the file: ")
    file.write(data)
    file.close()
    print("Data written to", filename)

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)
    print("File", old_name, "renamed to", new_name)

def delete_file(filename):
    os.remove(filename)
    print("File", filename, "deleted")

# Menu options
while True:
    print("1. Read file")
    print("2. Write to file")
    print("3. Rename file")
    print("4. Delete file")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        filename = input("Enter the name of the file to read: ")
        read_file(filename)
    elif choice == '2':
        filename = input("Enter the name of the file to write: ")
        write_file(filename)
    elif choice == '3':
        old_name = input("Enter the current name of the file: ")
        new_name = input("Enter the new name of the file: ")
        rename_file(old_name, new_name)
    elif choice == '4':
        filename = input("Enter the name of the file to delete: ")
        delete_file(filename)
    elif choice == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")
        