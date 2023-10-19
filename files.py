file_path = input("Enter the path to the text file: ")


with open(file_path) as file:
    text = file.read()
    words = text.split()  

word_count = len(words)

# Output: Display the word count
print(f"The number of words in the file '{file_path}' is: {word_count}")