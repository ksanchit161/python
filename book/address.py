# Read the address from the user
address = input("Enter your full address: ")

# Split the address into parts based on commas or spaces for multiple line display
# You can customize the delimiter as per your address format (commas, spaces, etc.)
address_lines = address.split(',')

# Print the address in multiple lines
print("\nYour address is:")
for line in address_lines:
    print(line.strip())  # strip() removes any extra spaces around the parts
