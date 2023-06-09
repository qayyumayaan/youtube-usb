def BinaryToColors(input_file, output_file):
    # Read the binary content from the input file
    with open(input_file, 'r') as file:
        binary_content = file.read()

    # Convert binary to colors
    color_content = bytearray()
    for i in range(0, len(binary_content), 2):
        bits = binary_content[i:i+2]
        if bits == '00':
            color_content.append(98)   # ASCII code for 'b'
        elif bits == '01':
            color_content.append(114)  # ASCII code for 'r'
        elif bits == '10':
            color_content.append(103)  # ASCII code for 'g'
        elif bits == '11':
            color_content.append(121)  # ASCII code for 'y'

    # Write the color content to the output file
    with open(output_file, 'wb') as file:
        file.write(color_content)

    print("Conversion from binary to colors completed!")

intermediary_form_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\intermediary_form.txt"
output_file_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\colors.txt"
BinaryToColors(intermediary_form_path, output_file_path)