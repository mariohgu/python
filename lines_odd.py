def delete_odd_lines(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Remove odd-numbered lines
    even_lines = [line for i, line in enumerate(lines) if i % 2 != 0]

    # Save the modified content back to the file
    with open(filename, 'w') as file:
        file.writelines(even_lines)


# Specify the path to the text file
file_path = '/home/wario/Documentos/python/lineas.txt'

# Call the function to delete odd lines
delete_odd_lines(file_path)