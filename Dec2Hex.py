import sys

def decimal_to_hex(decimal_value):
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            print(f"Hexadecimal representation is: {decimal_to_hex(decimal_value)}")
        except ValueError:
            print("Error: Please provide a valid integer.")
    else:
        print("Error: No input provided.")
