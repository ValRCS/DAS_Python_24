import itertools
import random
 
# vertiba = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'kalps', 'karaliene', 'karalis', 'tūzis']
vertiba = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# masts = ['ercens', 'kreics', 'kāravs', 'pīķis']
masts = '♠♣♥♦' # of course I could have used a list of all 4 suits
 
kava = list(itertools.product(vertiba, masts))
# print first 5
print(kava[:5])
random.shuffle(kava) # crucial that this is IN-PLACE
print("AFTER SHUFFLE")
print(kava[:5])
# for vertiba, masts in kava:
#     print(vertiba, masts)