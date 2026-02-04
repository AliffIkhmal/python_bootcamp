
#   string indexing and slicing
name = "Alice Wonderland"

print(name[0])          # First character
print(name[-1])         # Last character
print(name[0:5])       # Substring from index 0 to 4
print(name[6:])       # Substring from index 6 to end
print(name[:5])       # Substring from start to index 4
print(name[::-1])     # Reverse the string



#   string methods
text = "ice cream"

print(text.upper())                     # Convert to uppercase
print(text.lower())                     # Convert to lowercase
print(text.capitalize())                # Capitalize first letter
print(text.title())                     # Title case 
print(text.replace("ice", "oil"))       # Replace spaces with underscores
print(text.strip())                     # Remove leading/trailing whitespace
print(len(text))                        # Get the length of the string

#   string formatting
name = "Aliff"
age = 26

# Using f-strings
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

 Using str.format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

# Using % operator
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)

text = """Python is a powerful programming language. It's easy to learn and versatile.
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

# to count words
print(f"Number of words in the text: {len(text.split())}"   )

#to count characters excluding whitespaces
print(f"Number of characters excluding whitespaces in the text: {len(text.replace(' ', '').replace('\n', ''))}")

#to count characters including whitespaces
print(f"Number of characters including whitespaces in the text: {len(text)}")

#to count sentences
print(f"Number of sentences in the text: {len(text.split('.')) - 1}")
