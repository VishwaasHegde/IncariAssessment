from components.prompt_template import create_template
import os
import json
import requests
import logging
from evaluate.evaluate import Evaluate

class IncariUtil:

    def __init__(self):
        self.ollama_url = os.environ.get('INCARI_OLLAMA', 'http://ollama:11434')
        self.OLLAMA_MODEL = 'llama3.1'
        self.evaluate = Evaluate()

    def create_api_data(self, req_data):
        """
        Creates api specific data
        :param req_data: requirement
        :type req_data: str
        :return: dictionary to be fed to the LLM
        :rtype: dict
        """
        return {"model": self.OLLAMA_MODEL, "prompt": req_data, "stream": False}

    def generate_nodes(self, req_data):
        """
        Generates a sequence of nodes
        :param req_data: user requirement
        :type req_data: str
        :return: sequence of nodes
        :rtype: str
        """
        req_data = create_template(req_data)
        req_data = self.create_api_data(req_data)
        response = requests.post(url="{}/api/generate".format(self.ollama_url), data=json.dumps(req_data)).text
        response = json.loads(response)
        logging.info(response)
        return response['response']

    def evaluate_score(self, actual, predicted):
        """
        Evaluates the prediction and returns blue, rouge and minimum edit distance
        :param actual: target
        :type actual: str
        :param predicted: predictions
        :type predicted: str
        :return: dictionary of bleu, rouge and edit distance scores
        :rtype: dict
        """
        actual = actual.split()
        predicted = predicted.split()
        return self.evaluate.get_scores(actual, predicted)

