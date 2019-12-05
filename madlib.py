import fileinput
import re

#Madlib Game

def write_file(path, contents):
  with open(path, 'w') as f:
    f.write(contents)

def read_file(path):
  try:
    with open(path) as f:
      print(f.read())
  except FileNotFoundError as e:
    print('File not found', e)
  except ValueError as ve:
    print('Value Error', ve)

def get_name():
    name = input('Hello there. What is your name? ')
    print('Hello ' + name + ', let\'s play a game! I will ask you to type in certain types words. Hit enter after every word.')

word_type = ['adjective', 'adjective', 'first name', 'past tense verb', 'first name', 'adjective', 'adjective', 'plural noun', 'large animal', 'small animal', 'a girls name', 'adjective', 'plural noun', 'adjective', 'plural noun', 'number from 1 - 50', 'first name', 'number', 'plural', 'noun', 'number', 'plural noun']

user_input_list = []

def get_words():
    for elem in word_type:
        user_input = input('Enter ' + elem + ': ')
        user_input_list.append(user_input)
    print(user_input, user_input_list)

def write_words():
    for elem in word_type:
        write_file('madlib.txt', elem)

# from stackoverflow: https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file
with fileinput.FileInput('madlib.txt', inplace=True) as file:
    for line in file:
        print(line.replace('Adjective', 'I changed this word'), end='')

#loop through every word in txt and find { } and replace word inside with users input list


get_name()
get_words()

# read_file('madlib.txt')
# get_name()
# get_words()

#to start program
def start():
    pass

if __name__ == '__main__':
    start()


