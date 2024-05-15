# Uzrakstīt programmu teksta simbola atpazīšanai
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***
# Principā tas ir labs iesākums karātavu spēlei.

name = input("Ievadīt vārdu: ") # TODO idea get name from a list of names, from a file, from a web page
guess_count = 0
 
buffer = ""
for char in name:
    if char == " ": 
        buffer += char # could also be " "
    else: 
        buffer += "*"
print(buffer)
guess_so_far = buffer
guess_count += 1

while guess_so_far != name:
    buffer = ""
    guess = input("Ievadīet burtu : ") # TODO vai visu vārdu uzreiz
    # TODO add check for full word guess
    if len(guess) != 1: 
        print("Ievadīt precīzi vienu burtu!")
        continue # goes back to start of loop
    # we can use zip to iterate over two iterables at the same time
    # so we can iterate over the original name and the guess_so_far
    for original_char, current_char in zip(name, guess_so_far):
        if original_char == " ":
            buffer += " "
        elif original_char == guess:
            buffer += original_char # means we show the original character
        else:
            buffer += current_char # means we show the current character
    print(buffer)
    if buffer == guess_so_far:
        print("Burts nav šajā vārdā")
        # TODO show picture with hangman here could be ASCII art or some other way
    # for debugging
    # print("For debugging: ", name, guess_so_far, buffer)
    guess_so_far = buffer # rewrite the guess with the new buffer
    guess_count += 1
    # could add break here if we want to exit after some limit of guesses
    # TODO add MAX_GUESSES = 10 or some other number

print(f"Vārds {name} atminēts pēc {guess_count} mēģinājumiem!")