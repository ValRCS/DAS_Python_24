# 3. Apgrieztie vārdi
# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

sentence = input("Please enter your sentence!")
# reverse_sentence = sentence[::-1]
# words = reverse_sentence.split()
# print(words)
# words = words[::-1]
# # let's capitalize the first letter of the first word
# # assuming there is at least one word
# words[0] = words[0].capitalize()
# new_sentence = ' '.join(words)
# assuming there is at least one word

# alternative approach
words = sentence.split() # so we have a list of words
# reversed_words = [word[::-1] for word in words]
# below is the same as above, just using a for loop
reversed_words = []
for word in words:
    reversed_words.append(word[::-1])
new_sentence = ' '.join(reversed_words)
new_sentence = new_sentence.capitalize() # if we do not mind that rest of letters are lowercase

print(new_sentence) 