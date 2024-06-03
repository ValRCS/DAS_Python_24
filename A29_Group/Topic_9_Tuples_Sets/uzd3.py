# def is_pangram_loop(mytext, a = "abcdefghijklmnopqrstuvwxyz"):
#     mytext = mytext.lower().replace(" ", "") # replace is actually not needed in this case

#     for char in a:
#         if char not in mytext:
#             return False
#     return True

# let's do the same with sets
def is_pangram(mytext, a = "abcdefghijklmnopqrstuvwxyz"):
    return set(a) <= set(mytext.lower()) #same as  set(a).issubset(set(mytext.lower()))


print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
# anti example
print(is_pangram("The quick brown fox jumps over the lazy cat")) # False

# let's give Latvian alphabet
latvian_a = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
# first check length of alphabet
print(len(latvian_a)) # 33
print(is_pangram("Āboltiņš čukās, ģērbies, jūrā mētās", latvian_a))
print(is_pangram("Muļķa hipiji mēģina brīvi nogaršot celofāna žņaudzējčūsku.", latvian_a))
print(is_pangram("Četri balti krekli dzīvē jau skumji pārējā.", latvian_a))
