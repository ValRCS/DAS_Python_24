# ----------------
# Lietotājs(pirmais spēlētājs) ievada tekstu.
# Tiek izvadītas tikai zvaigznītes burtu vietā. Pieņemsim, ka cipari nebūs, bet atstarpes gan var būt
# Lietotājs(tātad otrs spēlētājs) ievada simbolu. 
# Ja burts ir tad tas burts attiecīgajās vietās tiek parādīts, visi pārējie burti paliek par zvaigznītēm.
# Kartupeļu lauks -> ********* *****
# ievada a -> *a****** *a***

txt = input("Lūdzu ievadiet tekstu: ")

new_txt = ''
for letter in txt:
    if letter == ' ':
        new_txt += letter # could have also used ' '
    else:
        new_txt += '*'
print(new_txt)


# while True:
#     simb = input("Lūdzu ievadiet simbolu: ")
#     if len(simb)==1:
#         break
#     print("Atļauts tikai viens simbols. ")
        
# result = ''
# for letter in txt:
#     if letter == ' ' or letter == simb:
#         result += letter 
#     else:
#         result += '*'
        
# print(result)

# we could loop with while until new_txt is equal to txt

while new_txt != txt:
    simb = input("Lūdzu ievadiet simbolu: ")
    if len(simb)==1:
        result = ''
        # i need to loop through BOTH txt and new_txt
        # we can use zip function to loop through two lists at the same time
        # zip will run until the shortest iterable is exhausted
        for txt_letter, new_txt_letter in zip(txt, new_txt):
            if txt_letter == simb:
                result += simb # could use txt_letter 
            else:
                result += new_txt_letter

        print(result)
        new_txt = result
    else:
        print("Atļauts tikai viens simbols. ")

# TODO: add a check if the letter is already in the new_txt 
# TODO add counter for the number of tries
# add initial MAX_TRIES = 5
# TODO add display of the situation/state of the game
# this could ASCII art of a hangman or even some graphics (later on that)
# TODO reading of possible words from a file for Player versus Computer
# TODO read list of words from internet