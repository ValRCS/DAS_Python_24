# 3. Apgrieztie vārdi
sentence = input("Please write some short sentence of any kind ")
words = sentence.split()
reverse_sentence = []
for word in words:
    reverse_sentence.append(word[::-1])
 
final_output = " ".join(reverse_sentence).capitalize()
# bonus section
# special_characters = [".", "!", "?"]
end_chars = ".!?" # could use list but string is easier to work with
for char in end_chars:
    if char in final_output:
        final_output = final_output.replace(char, "") 
        final_output += char # here we add the char back to the end of the sentence
        break # assuming there is only one end char

print(final_output)