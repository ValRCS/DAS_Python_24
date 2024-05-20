# 2. Palindroms
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira    sula") -> True


def is_palindrome(text: str) -> bool:
    text=text.lower()
    text=text.replace(" ","") # so any whitespace is removed
    rev_text=text[::-1]

    return rev_text==text
    # no need for if else since rev_text==text will return True or False
    # if rev_text==text:
    #     return True
    # else:
    #     return False
    
    
# ievads=input("Ievadiet kaut kādu tekstu: ")
# print(is_palindrome(ievads))

print(is_palindrome("Alus ari ira    sula")) # True
print(is_palindrome(" ABBBa   ")) # True
# counterexample
print(is_palindrome("Valdis")) # False