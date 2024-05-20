# 3.uzd - teksta pārveidošana
 
keyword_1 = "nav"
keyword_2 = "slikt"
new_part = "ir lab"
# keyword_3 = "slikta"
name = input("Ievadīt vārdu: ")
start = name.find(keyword_1)
# start = name.index(keyword_1) # would need try except block
finish = name.rfind(keyword_2)
# finish_2 = name.rfind(keyword_3)
# print(finish, finish_2)

# new_part_2 = "ir laba"
if start == -1 or finish == -1 or start >= finish:
    print("Kāds no vārdiem nav atrasts vai arī sākuma vārds ir pēc beigu vārda!")
    # print original name
    print(name)
else:
    print(name[:start] + new_part + name[finish + len(keyword_2):])

# same would be done with where we start with the modification
if start != -1 and finish != -1 and start < finish:
    print(name[:start] + new_part + name[finish + len(keyword_2):])
else:
    # print original
    print(name)