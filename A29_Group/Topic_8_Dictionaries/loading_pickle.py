# let's load our dictionary from the file
import pickle
with open('phonebook.pickle', 'rb') as file:
    my_dict = pickle.load(file)

print(my_dict)

