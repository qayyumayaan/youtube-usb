def convert_to_binary(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    binary_content = ''.join(format(ord(char), 'b') for char in content)

    with open(output_file, 'w') as file:
        file.write(binary_content)

    print("Conversion completed!")

input_file_path = r"C:\Users\amazi\Downloads\Digital to YouTube.txt"
output_file_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\output.txt"

# input_file_path = input("Input: ")

# output_file_path = input("Output: ")

convert_to_binary(input_file_path, output_file_path)
