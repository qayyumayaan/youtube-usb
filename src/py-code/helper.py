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
                    color_content.append(ord("D"))
                else:
                    color_content.append(ord("B"))
            else:
                if bits[2] == '0':
                    color_content.append(ord("G"))
                else:
                    color_content.append(ord("C"))
        else:
            if bits[1] == '0':
                if bits[2] == '0':
                    color_content.append(ord("R"))
                else:
                    color_content.append(ord("P"))
            else:
                if bits[2] == '0':
                    color_content.append(ord("Y"))
                else:
                    color_content.append(ord("W"))
   
   
    # Write the color content to the output file
    with open(output_file, 'wb') as file:
        file.write(color_content)

    print("Conversion from binary to colors completed!")


def ColorsToBinary(input_file, output_file):
    # Read the colored content from the input file
    with open(input_file, 'rb') as file:
        color_content = file.read()

    # Convert colors to binary
    binary_content = ""
    for color in color_content:
        if color == ord("D"):
            binary_content += "000"
        elif color == ord("B"):
            binary_content += "001"
        elif color == ord("G"):
            binary_content += "010"
        elif color == ord("C"):
            binary_content += "011"
        elif color == ord("R"):
            binary_content += "100"
        elif color == ord("P"):
            binary_content += "101"
        elif color == ord("Y"):
            binary_content += "110"
        elif color == ord("W"):
            binary_content += "111"

    # Write the binary content to the output file
    with open(output_file, 'w') as file:
        file.write(binary_content)

    print("Conversion from colors to binary completed!")


input_file_path = r"C:\Users\amazi\Downloads\Youtube data.png"
intermediary_form_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\intermediary_form.txt"
output_file_path = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\colors.txt"

output_output = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\coloredTemp.bin"

output_output_out = r"C:\Users\amazi\Documents\GitHub\youtube-usb\src\py-code\coloredFinal.png"


from main import BinaryToFile, FileToBinary

FileToBinary(input_file_path, intermediary_form_path)

BinaryToColors(intermediary_form_path, output_file_path)
ColorsToBinary(output_file_path, output_output)

BinaryToFile(output_output, output_output_out)



