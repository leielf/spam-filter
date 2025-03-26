from trainingcorpus import TrainingCorpus
import os
from utils import read_classification_from_file
import math
from typing import Dict

SPAM_TAG = "SPAM"
HAM_TAG = "OK"

ham_path = "trained_ham_words.txt"
spam_path = "trained_spam_words.txt"


class MyFilter:
    def __init__(self):
        self.spam_words = {}
        self.ham_words = {}
        self.training_corpus = TrainingCorpus()

    def train(self, path: str):
        truth = read_classification_from_file(os.path.join(path, "!truth.txt"))
        name_content_dict = self.training_corpus.emails(path)
        # keys: words in spam emails; values: number of emails in which this word occurs
        self.spam_words = self.training_corpus.get_number_of_emails(self.training_corpus.spams(truth, name_content_dict).values())
        # keys: words in ham emails; values: number of emails in which this word occurs
        self.ham_words = self.training_corpus.get_number_of_emails(self.training_corpus.hams(truth, name_content_dict).values())

    def read_file(self, path: str, words: Dict[str, int]):
        with open(path, encoding="utf-8") as f:
            for line in f.readlines():
                if line.split(' ')[0] not in words.keys():
                    words[line.strip('\n').split(' ')[0]] = int(line.strip('\n').split(' ')[1])
                else:
                    words[line.strip('\n').split(' ')[0]] += int(line.strip('\n').split(' ')[1])

    def test(self, emails_dir: str):
        """
        naive Bayes
        using formula ln(1/p - 1) = ... calculating this number for both ham and spam words
        if the result calculated with spam words is LESSER than the result calculated with ham words,
        then this email is SPAM. Otherwise, it is HAM
        """
        name_content_dict = self.training_corpus.emails(emails_dir)
        self.read_file(spam_path, self.spam_words)
        self.read_file(ham_path, self.ham_words)
        predictions = {}
        ham_amount = sum(self.ham_words.values())
        spam_amount = sum(self.spam_words.values())
        self.training_corpus.compare_words(self.spam_words, self.ham_words)
        tag = ''
        for name, content in name_content_dict.items():
            words = self.training_corpus.get_words_from_email(content)
            sum_value_spam = 0
            sum_value_ham = 0
            for word in words:
                if word in self.spam_words.keys():
                    p = self.spam_words[word] / spam_amount
                    sum_value_spam += (math.log(1 - p) - math.log(p))
                    p_h = self.ham_words[word] / ham_amount
                    sum_value_ham += (math.log(1 - p_h) - math.log(p_h))
            if sum_value_spam <= sum_value_ham:
                tag = SPAM_TAG
            else:
                tag = HAM_TAG
            predictions[name] = tag
        path = os.path.join(emails_dir, "!prediction.txt")
        with open(path, "w", encoding="utf-8") as f:
            for key, value in predictions.items():
                f.writelines([key, " ", value, "\n"])
