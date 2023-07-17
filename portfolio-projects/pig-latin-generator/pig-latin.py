print("Please input a phrase you would like to convert to pig latin:")
string = input().lower()
words = string.split()
translated = []

vowels = ['a', 'e', 'i', 'o', 'u']

for word in words:
    if word[0] in vowels:
        translated.append(word + "yay")
    elif any(letter in vowels for letter in word):
        for ind in range(len(word)):
            if word[ind] in vowels:
                translated.append(word[ind:] + word[:ind] + "ay")
                break
    else:
        translated.append(word + "ay")

res = ' '.join(translated)
print(res)
