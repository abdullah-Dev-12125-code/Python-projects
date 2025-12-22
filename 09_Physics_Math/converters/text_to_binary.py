def text_to_binary(text):
    return ' '.join(format(ord(c), '08b') for c in text)

text = input("Enter text: ")
print(text_to_binary(text))
