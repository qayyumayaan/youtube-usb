def FileToBinary(input_file, output_file):
    with open(input_file, 'rb') as file:
        content = file.read()

    binary_content = ''.join(format(byte, '08b') for byte in content)

    with open(output_file, 'w') as file:
        file.write(binary_content)

    print("Conversion to binary completed!")
    
def BinaryToFile(input_file, output_file):
    # Read the binary content from the input file
    with open(input_file, 'r') as file:
        binary_content = file.read()

    # Convert binary to characters
    text_content = bytearray()
    for i in range(0, len(binary_content), 8):
        byte = binary_content[i:i+8]
        text_content.append(int(byte, 2))

    # Write the text content to the output file
    with open(output_file, 'wb') as file:
        file.write(text_content)

    print("Conversion from binary to file completed!")
