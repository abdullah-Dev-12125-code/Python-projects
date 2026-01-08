import random

fragments = ["Py","tho","nPro","gram","ming"]
word ="".join(fragments)
print(word[:6], word[6:])
print(word[2:10] + word[:2] + word[11:16])
print(len(word))

list_word = list(word)
shuffling = random.shuffle(list_word)
shuffled_word = "".join(list_word)
print(shuffled_word)