text = input("Enter your text here: ")
vowels = 'aeiouAEIOU'

for i in range(len(text)):
    if text[i] in vowels:
        print(f"Vowel '{text[i]}' found at position {i+1}")

