import os

def list_files():
    files = os.listdir('.')
    for file in files:
        print(file)

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

def current_directory():
    print(f"Current directory: {os.getcwd()}")

def main():
    while True:
        print("\nLinux Terminal Helper")
        print("1. List files")
        print("2. Create directory")
        print("3. Show current directory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_files()
        elif choice == '2':
            directory_name = input("Enter the directory name: ")
            create_directory(directory_name)
        elif choice == '3':
            current_directory()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()