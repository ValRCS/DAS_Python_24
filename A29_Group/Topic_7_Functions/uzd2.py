# 2. Palindroms

# uzrakstiet funkciju is_palindrome(text)

# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.

# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus

# is_palindrome("Alus ari ira      sula") -> True

def is_palindrome(text:str|int, debug=False) -> bool:
    """
    Function to check if text is a palindrome
    text - can be a string or an integer
    debug - if True will print out intermediate results
    returns True if text is a palindrome, False otherwise
    """
    text = str(text) # could have used another variable but no need
    tokens = text.split() # possible to have a list with one element if no spaces
    result = " ".join(tokens).lower() 
    if debug:
        print(f"Initial text: {text}")
        print(f"Tokens: {tokens}")
        print(f"Result: {result}")
        print(f"Revers: {result[::-1]}")
    return result == result[::-1] # we can do this because we expect boolean result anyway
    
print(is_palindrome("Alus ari ira      sula"))
# let's test out numbers
print(is_palindrome(12321)) # True
print(is_palindrome(12345)) # False
# Valdis
print(is_palindrome("Valdis")) # False

# let's add debug
print(is_palindrome("Alus ari ira      sula", debug=True))