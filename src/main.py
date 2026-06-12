import os

def create_note():
    title = input("Enter note title: ")

    if not validate_title(title):
        return "Invalid title. Filenames cannot contain <, >, :, \", /, \\, |, ?, or *."

    print("Enter note content (Type END on a new line when finished.):")
    
    content_lines = []
    while True:
        line = input()
        if line == "END":
            break
        content_lines.append(line)
        
    content = "\n".join(content_lines)
    
    directory = "notes"
    filepath = os.path.join(directory, f"{title}.txt")
    
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError:
            return "file path error"
    
    if os.path.exists(filepath):
        return "A note with this title already exists."
    
    try:
        with open(filepath, "w") as file:
            file.write(f"{content}")
        return "Note created successfully."
    except OSError:
        return "file path error"

def validate_title(title):
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        if char in title:
            return False
    return True

def list_notes():
    return "Feature not implemented"

def read_note():
    return "Feature not implemented"

def delete_note():
    return "Feature not implemented"

def show_menu():
    print("1. Create Note")
    print("2. List Notes")
    print("3. Read Note")
    print("4. Delete Note")
    print("5. Exit")
    
    user_input = input("Choose an option: ")
    choice = int(user_input) 
    
    if choice == 1:
        print(create_note())
    elif choice == 2:
        print(list_notes())
    elif choice == 3:
        print(read_note())
    elif choice == 4:
        print(delete_note())
    elif choice == 5:
        print("Goodbye!")
        return False
    else:
        print("Invalid input. Only integer input between 1 and 5 is allowed.")
        
    return True

def main():
    while True:
        try:
            should_continue = show_menu()
            if not should_continue:
                break
        except ValueError:
            print("Invalid input. Only integer input is allowed.")

if __name__ == "__main__":
    main()