filename = 'wash2.txt'
delete_until_row = 217500

with open(filename, 'r') as file:
    lines = file.readlines()

# Check if the file has enough rows to delete
if delete_until_row <= len(lines):
    updated_lines = lines[delete_until_row:]

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
        print(f"Rows 1 to {delete_until_row} deleted successfully.")
else:
    print("File doesn't have enough rows to delete.")