
    # multiple of 7
# for i in range (7, 100, 7):
#     print(i)


word = "python programming"
vowel = "aeiou"
vowel_count = 0
for character in word:
    if(character in vowel):
        vowel_count += 1

print(vowel_count)