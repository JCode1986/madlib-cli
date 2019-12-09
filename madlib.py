import re

#Madlib Game

def get_template_text(path):
    with open(path, 'r') as file:
        return(file.read())

def get_name():
    name = input('Hello there. What is your name? ')
    print('Hello ' + name + ', let\'s play a game! I will ask you to type in certain types of words. Hit enter after every word.')

user_input = []

def prompts(string):
    get_name()
    word_type = []
    word_type += re.findall(r"(?<={)[\w<>' -]+(?=})", string)
    for word in word_type:
        user_input.append(input('Enter ' + word + ': '))
    return user_input

def new_string(lst, string):
    remove_string_str_between_curlies = re.sub((r"(?<={)[\w<>' -]+(?=})"), '', string)
    final_string = remove_string_str_between_curlies.format(*lst)
    return final_string

def write_file_results(string, path, contents):
  with open(path, 'w') as f:
    f.write(string)

def start():
    str_from_template = get_template_text('template.txt')
    prompts(str_from_template)
    final_string = new_string(user_input, str_from_template)
    write_file_results(final_string, './madlib.txt', 'w')
    print(final_string)

if __name__ == '__main__':
    start()
