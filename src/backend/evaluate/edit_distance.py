import nltk

class EditDistance:

    def __init__(self):
        pass

    def get_scores(self, actual, predicted):
        """
        Evaluates the prediction and returns minimum edit distance
        :param actual: target
        :type actual: str
        :param predicted: predictions
        :type predicted: str
        :return: dictionary of edit distance scores
        :rtype: dict
        """
        return nltk.edit_distance(actual, predicted)