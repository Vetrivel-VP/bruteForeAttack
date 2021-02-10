import random
import pyautogui
import string

# chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
chars = string.printable
char_list = list(chars)
# print(char_list)
password = pyautogui.password('Enter the password :')
guess_password = ""

while (guess_password != password):
    guess_password = random.choices(char_list, k=len(password))

    print(f'<===={str(guess_password)}====>')

    if (guess_password == list(password)):
        print(f'Your password is {guess_password}')
        break
