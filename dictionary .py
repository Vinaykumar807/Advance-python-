# Open the text file in write mode
file = open("student.txt", "w")

# Write contents to the file
file.write("This is my sample file.\n")
file.write("This file contains Python data.")

# Close the file
file.close()

# Open the text file in read mode
file = open("student.txt", "r")

# Read the contents of the file
content = file.read()

# Display the contents
print("Contents of the file:")
print(content)

# Close the file
file.close()