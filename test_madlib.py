from madlib import get_template_text, get_name, prompts, new_string, write_file_results
import pytest


def test_get_template():
    expected = 'Remove the string inside the curly brackets {regex}'
    actual = get_template_text('./test.txt')
    assert actual == expected
    pass

def test_prompt_words_from_template(string):
    # expected = 1
    # actual = prompts('string')
    # assert actual == expected
    pass