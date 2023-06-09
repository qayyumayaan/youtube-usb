def BinaryToColors(input_file, output_file):
    # Read the binary content from the input file
    with open(input_file, 'r') as file:
        binary_content = file.read()

    # Convert binary to colors
    color_content = bytearray()
    for i in range(0, len(binary_content), 3):
        bits = binary_content[i:i+3]
        if bits[0] == '0':
            if bits[1] == '0':
                if bits[2] == '0':
                    print("000")
                else:
                    print("001")
            else:
                if bits[2] == '0':
                    print("010")
                else:
                    print("011")
        else:
            if bits[1] == '1':
                if bits[2] == '0':
                    print("100")
                else:
                    print("101")
            else:
                if bits[2] == '0':
                    print("110")
                else:
                    print("111")
   
   
    # Write the color content to the output file
    with open(output_file, 'wb') as file:
        file.write(color_content)

    print("Conversion from binary to colors completed!")

intermediary_form_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\intermediary_form.txt"
output_file_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\colors.txt"
BinaryToColors(intermediary_form_path, output_file_path)