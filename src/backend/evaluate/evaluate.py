from evaluate.bleu import Bleu
from evaluate.rouge import Rouge
from evaluate.edit_distance import EditDistance

# from bleu import Bleu
# from rouge import Rouge
# from edit_distance import EditDistance

class Evaluate:

    def __init__(self):
        self.bleu = Bleu()
        self.rouge = Rouge()
        self.edit_distance = EditDistance()

    def get_scores(self, actual, predicted):
        """
        Evaluates the prediction and returns blue, rouge and minimum edit distance
        :param actual: target
        :type actual: str
        :param predicted: predictions
        :type predicted: str
        :return: dictionary of bleu, rouge and edit distance scores
        :rtype: dict
        """

        bleu_score = self.bleu.get_scores(actual, predicted)
        rouge_score = self.rouge.get_scores(actual, predicted)
        ed_score = self.edit_distance.get_scores(actual, predicted)
        bleu_score, rouge_score, ed_score = round(bleu_score, 2), round(rouge_score, 2), round(ed_score, 2)
        return bleu_score, rouge_score, ed_score



