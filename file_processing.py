filename = input("Enter the name of your text file: ")

if not filename.endswith('.txt'):
    filename += '.txt'
    print(f"Added .txt extension. Looking for file: {filename}")

try:
    with open(filename, 'r') as file:
        text = file.read()
    
    # Convert text to uppercase
    uppercase_text = text.upper()
    
    # Create new filename
    modifiedfile = filename.replace('.txt', '_uppercase.txt')
    
    # Write the uppercase text to new file
    with open(modifiedfile, 'w') as new_file:
        new_file.write(uppercase_text)
    
    print(f"\nSuccess! Your new file '{modifiedfile}' has been created.")
    print(f"Original file size: {len(text)} characters")
    print("All the text has been converted to uppercase!")

except FileNotFoundError:
    print(f"\nError: Could not find the file '{filename}'")
    print("Please make sure:")
    print("1. The file exists in the current directory")
    print("2. You typed the name correctly")
    print("3. You included the .txt extension (or we'll add it for you)")

except Exception as e:
    print(f"\nSomething went wrong: {str(e)}")
    print("Please try again!") 