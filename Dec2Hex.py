import sys

def dec_to_hex(decimal):
    return hex(decimal)[2:].upper()

if __name__ == "__main__":
    # Check if an input argument is provided
    if len(sys.argv) < 2:
        print("Error: No input provided. Please enter an integer.")
        sys.exit(1)  # Exit with error

    try:
        # Try to convert input to integer
        decimal_number = int(sys.argv[1])
        print(f"Hexadecimal representation is: {dec_to_hex(decimal_number)}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        sys.exit(1)  # Exit with error
