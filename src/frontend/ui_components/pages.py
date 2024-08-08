import os
import requests
import json

backend_url = os.environ.get('INCARI_BACKEND', 'http://incariengine:8025')


def code_chat(requirement: str):
    """
    Creates api specific data
    :param requirement: requirement
    :type requirement: str
    :return: dictionary to be fed to the LLM
    :rtype: dict
    """
    view_request = {"requirement":requirement}
    response = requests.post(url="{}/chat".format(backend_url), data=json.dumps(view_request)).text
    # logging.warning('code_chatcode_chat', str(response))
    response = json.loads(response)
    return response

def evaluate(actual, predicted):
    """
    Evaluates the prediction and returns blue, rouge and minimum edit distance
    :param actual: target
    :type actual: str
    :param predicted: predictions
    :type predicted: str
    :return: dictionary of bleu, rouge and edit distance scores
    :rtype: dict
    """

    view_request = {"actual": actual, 'predicted': predicted}
    response = requests.post(url="{}/evaluate".format(backend_url), data=json.dumps(view_request)).text
    response = json.loads(response)
    return response['response']