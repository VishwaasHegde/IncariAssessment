# tests/test_incari.py

import os
import requests
import json
import re

backend_url = os.environ.get('INCARI_BACKEND', 'http://incariengine:8025')
ollama_url = os.environ.get('INCARI_OLLAMA', 'http://ollama:11434')

def evaluate(actual, predicted):
    view_request = {"actual": actual, 'predicted': predicted}
    response = requests.post(url="{}/evaluate".format(backend_url), data=json.dumps(view_request)).text
    response = json.loads(response)
    return response['response']

def run_backend(requirement):
    view_request = {"requirement": requirement}
    response = requests.post(url="{}/chat".format(backend_url), data=json.dumps(view_request)).text
    # logging.warning('code_chatcode_chat', str(response))
    response = json.loads(response)
    return response['response']

def parse_output(response):
    pat = '\\[(\\w*)\\]'
    pat_find = re.findall(pat, response)
    return pat_find


def test_backend_1():
    requirement = 'Navigate to a new page after a delay of 3 seconds when the user clicks a button.'
    actual = ['OnClick', 'Delay', 'Navigate']
    response = run_backend(requirement)
    response = parse_output(response)
    assert actual == response

def test_backend_2():
    requirement = 'Log a message when a key is pressed and display the key value on the screen.'
    actual = ['OnKeyPress', 'Log', 'Show']
    response = run_backend(requirement)
    response = parse_output(response)
    assert actual == response

def test_backend_3():
    requirement = 'Reduce a list of scores to find the highest score and log the result.'
    actual = ['Reduce', 'Log']
    response = run_backend(requirement)
    response = parse_output(response)
    assert actual == response


def test_backend_4():
    actual = '[OnClick] [Delay] [Navigate]'
    predicted = '[OnClick] [Delay] [Navigate]'
    score = evaluate(actual, predicted)
    bleu, rouge, ed_dist = score['BLEU'], score['ROUGE'], score['EDIT_DISTANCE']

    assert bleu == 1
    assert rouge == 1
    assert ed_dist == 0

def test_backend_5():
    actual = '[OnClick] [Delay] [Navigate]'
    predicted = '[OnClick] [Delay]'
    score = evaluate(actual, predicted)
    bleu, rouge, ed_dist = score['BLEU'], score['ROUGE'], score['EDIT_DISTANCE']

    assert 0.5 <= bleu < 0.7
    assert 0.7 <= rouge < 0.9
    assert ed_dist == 1

def test_backend_6():
    actual = '[OnClick] [Delay] [Navigate]'
    predicted = '[Reduce] [Log]'
    score = evaluate(actual, predicted)
    bleu, rouge, ed_dist = score['BLEU'], score['ROUGE'], score['EDIT_DISTANCE']

    assert bleu==0
    assert rouge==0
    assert ed_dist == 3

def test_backend_7():
    requirement = 'Navigate to a new page when the user clicks a button.'
    actual = ['OnClick', 'Navigate']
    response = run_backend(requirement)
    response = parse_output(response)
    assert actual == response
