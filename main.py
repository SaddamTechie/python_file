def read_and_modify_file():
    original_file = input("Enter the filename to read: ")
    modified_file = "modified_" + original_file

    try:
        # Attempt to open the input file for reading
        with open(original_file, 'r') as file:
            # Read content from the file
            content = file.read()
            print("Original content of the file !")
            print(content)
            
            # Modify content (e.g., convert to uppercase)
            new_content = input("Enter Content to add to the modified version!")
            
            # Write modified content to a new output file
            with open(modified_file, 'w') as new_file:
                new_file.write(content+'\n'+new_content)
                print(f"Modified content written to {modified_file}.")

    except FileNotFoundError:
        print(f"Error: The file '{original_file}' does not exist.")
    except IOError:
        print(f"Error: The file '{original_file}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()
