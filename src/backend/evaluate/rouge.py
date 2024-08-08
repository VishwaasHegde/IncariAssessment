from collections import Counter
from itertools import islice

class Rouge:

    def __init__(self):
        pass

    def ngrams(self, sequence, n):
        """
        Generate n-grams from a sequence of words.
        :param sequence: The input sequence of words.
        :type sequence: list
        :param n: The number of items in each n-gram.
        :type n: int
        :return: A list of n-grams.
        :rtype: list
        """
        return list(zip(*(islice(sequence, i, None) for i in range(n))))

    def calculate_rouge_n(self, predicted, actual, n=1):
        """
        Calculate ROUGE-N score between predicted and actual sequences.
        :param predicted: The predicted list of words.
        :type predicted: list
        :param actual: The reference list of words.
        :type actual: list
        :param n: The n-gram level to calculate the ROUGE score (default is 1 for ROUGE-1).
        :type n: int
        :return: Precision, recall, and F1-score for ROUGE-N.
        :rtype: dict
        """
        pred_ngrams = Counter(self.ngrams(predicted, n))
        actual_ngrams = Counter(self.ngrams(actual, n))

        overlap = sum((pred_ngrams & actual_ngrams).values())
        pred_total = sum(pred_ngrams.values())
        actual_total = sum(actual_ngrams.values())

        precision = overlap / pred_total if pred_total > 0 else 0.0
        recall = overlap / actual_total if actual_total > 0 else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

        return {"precision": precision, "recall": recall, "f1": f1}


    def get_scores(self, actual, predicted):
        """
        Evaluates the prediction and returns rouge score (average)
        :param actual: target
        :type actual: str
        :param predicted: predictions
        :type predicted: str
        :return: dictionary of rouge scores
        :rtype: dict
        """

        rouge_sc = 0
        for n in range(1, len(actual)+1):
            r = self.calculate_rouge_n(predicted, actual, n=1)
            rouge_sc += r['f1']
        return rouge_sc/len(actual)