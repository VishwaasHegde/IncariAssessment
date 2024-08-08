from collections import Counter
import numpy as np


class Bleu:


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
        return list(zip(*(sequence[i:] for i in range(n))))

    def modified_precision(self, predicted, references, n):
        """
        Calculate modified n-gram precision for a given n.
        :param predicted: The predicted word sequence.
        :type predicted: list
        :param references: The list of reference word sequences.
        :type references: list
        :param n: The n-gram level to calculate precision for.
        :type n: int
        :return: The modified precision.
        :rtype: float
        """
        pred_ngrams = Counter(self.ngrams(predicted, n))
        max_ref_ngrams = Counter()

        for reference in references:
            ref_ngrams = Counter(self.ngrams(reference, n))
            for ngram in pred_ngrams:
                max_ref_ngrams[ngram] = max(max_ref_ngrams[ngram], ref_ngrams[ngram])

        overlap = sum(min(count, max_ref_ngrams[ngram]) for ngram, count in pred_ngrams.items())
        total_pred_ngrams = sum(pred_ngrams.values())

        return overlap / total_pred_ngrams if total_pred_ngrams > 0 else 0.0

    def brevity_penalty(self, predicted, references):
        """
        Calculate the brevity penalty for predicted and reference sequences.
        :param predicted: The predicted word sequence.
        :type predicted: list
        :param references: The list of reference word sequences.
        :type references: list
        :return: The brevity penalty.
        :rtype: float
        """
        pred_len = len(predicted)
        ref_lens = [len(reference) for reference in references]

        closest_ref_len = min(ref_lens, key=lambda ref_len: (abs(ref_len - pred_len), ref_len))

        if pred_len > closest_ref_len:
            return 1
        elif pred_len == 0:
            return 0
        else:
            return np.exp(1 - closest_ref_len / pred_len)

    def calculate_bleu(self, predicted, references, max_n=4):
        """
        Calculate the BLEU score for a predicted sequence against reference sequences.
        :param predicted: the predicted word sequence.
        :type predicted: list
        :param references: The list of reference word sequences.
        :type references: list
        :param max_n: The maximum n-gram length to consider (default is 4).
        :type max_n: int
        :return: The BLEU score.
        :rtype: float
        """

        precisions = [self.modified_precision(predicted, references, n) for n in range(1, max_n + 1)]

        # If all precisions are zero, return zero to avoid math error in log computation
        if all(p == 0 for p in precisions):
            return 0.0

        # Calculate geometric mean of precisions
        geometric_mean = np.exp(sum(np.log(p) for p in precisions if p > 0) / max_n)

        bp = self.brevity_penalty(predicted, references)

        return bp * geometric_mean


    def get_scores(self, actual, predicted):
        """
        Evaluates the prediction and returns bleu score
        :param actual: target
        :type actual: str
        :param predicted: predictions
        :type predicted: str
        :return: dictionary of bleu scores
        :rtype: dict
        """
        print([actual])
        print(predicted)
        bleu_score = self.calculate_bleu(predicted, [actual])
        return bleu_score
