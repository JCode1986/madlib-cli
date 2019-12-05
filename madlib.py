import fileinput
import re

#Madlib Game

#write to file
def write_file(path, contents):
  with open(path, 'w') as f:
    f.write(contents)

#read template text
def get_template_text(path):
    with open(path, 'r') as file:
        return(file.read())

#get user's name; instruction on what to do
def get_name():
    name = input('Hello there. What is your name? ')
    print('Hello ' + name + ', let\'s play a game! I will ask you to type in certain types words. Hit enter after every word.')

#hard coded for now..
word_type = ['adjective', 'adjective', 'first name', 'past tense verb', 'first name', 'adjective', 'adjective', 'plural noun', 'large animal', 'small animal', 'a girls name', 'adjective', 'plural noun', 'adjective', 'plural noun', 'number from 1 - 50', 'first name', 'number', 'plural', 'noun', 'number', 'plural noun']

#user input to replace strings with wrapped in {}
user_input_list = []

#find {'string here'}
def parse_template_text(template_text):
    pass

template = 'template.txt'
get_template_text(template)
template_string = get_template_text(template)

def get_words():
    for elem in word_type:
        user_input = input('Enter ' + elem + ': ')
        user_input_list.append(user_input)
    print(user_input, user_input_list)

def write_words(lst):
    for elem in lst:
        write_file('madlib.txt', elem)

#regex replace words with {}
with fileinput.FileInput('madlib.txt', inplace=True) as file:
    for line in file:
        line = re.sub(r"\{(.*?)\}", 'user inputs go here somehow', line)
        print(line)

def start():
    get_name()
    get_template_text(template)
    get_words()

if __name__ == '__main__':
    start()


