def write_to_file(content):
    try:
        with open("db.txt", "a") as file:
          file.write(f"Hello, {content}!")    # Write the original content back (if needed)
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("An error occurred while accessing the file.")
        

def read_from_file():
    try:
         with open("db.txt", "r+") as file:
            content = file.read()
            print(content)
            return content
    except FileNotFoundError:
        print("File not found!")
    except IOError:
        print("An error occurred while accessing the file.")

# Call the function to test it
read_from_file()
write_to_file("Aya")
