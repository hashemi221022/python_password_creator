
import string
import random
import os
def clear():
    os.system("clear")
clear()
def material_of_pass(): #? create character
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = list(string.ascii_uppercase)
    number = list(string.digits)
    simbol = ['!', '@', '#', '$', '%', '^', '&', '*']
    return upper_alphabet, lower_alphabet, number, simbol
uppalph, lowalph, num, simbol = material_of_pass()



def set_setting(): #? get input to set settings
    upper_choice = input("do you want upper alphabet in your pass ? (Yes, No)")
    lower_choice = input("do you want lower alphabet in your pass ? (Yes, No)")
    number_choice = input("do you want number in your pass ? (Yes, No)")
    simbol_choice = input("do you want simbol in your pass ? (Yes, No)")
    return upper_choice, lower_choice, number_choice, simbol_choice



def True_False(): #? convert yes or no to True or False
    list_of_True_False = []
    list_of_yes_no = list(set_setting())
    
    for char in list_of_yes_no:
        if (char == 'yes') or (char == 'Yes') or (char == 'Y') or (char == 'y'):
            list_of_True_False.append(True)
        else:
            list_of_True_False.append(False)
    return tuple(list_of_True_False)
a, b, c, d = True_False()



def user_choice(): #? character selection by user selection
    list_of_user_choice = []
    if a == True:
       list_of_user_choice.append(uppalph)
    if b == True:
        list_of_user_choice.append(lowalph)
    if c == True:
        list_of_user_choice.append(num)
    if d == True:
        list_of_user_choice.append(simbol)
    return list_of_user_choice



def final_choice(): #? put the character in the single list
    list_of_char = []
    for i in user_choice():
        for j in i:
            list_of_char.append(j)
    return list_of_char
        


def random_create_pass(list_of_char= final_choice(), number_of_char= 8, number_of_pass= 10): #? generate passwords through user inputs

    """
    first args: you can give a list of character
    second arg: you can give the number of character in your password
    third arg: you can give the number of password that you want to create
    """

    for _ in range(number_of_pass):
        password = []
        for _ in range(number_of_char):
            password.append(random.choice(list_of_char))
        print("".join(password))


random_create_pass()
# random_create_pass(final_choice(), 12, 5)
# help(random_create_pass)

# characters = ["n",'n','k', 'i']
# random_create_pass(characters, 15, 10)
