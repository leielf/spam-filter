from corpus import Corpus
from typing import Dict

SPAM_TAG = "SPAM"
HAM_TAG = "OK"


class TrainingCorpus(Corpus):
    def __init__(self):
        self.spam_words = {}
        self.ham_words = {}

    def get_number_of_emails(self, contents) -> Dict[str, int]:
        """
        creates a dictionary where keys are words from emails
        and values are the number of emails which have this word in it
        :param contents: list of emails content
        :return: emails_with_words
        """
        emails_with_words = {}
        for content in contents:
            content_words = self.get_words_from_email(content)
            for word in content_words.keys():
                if word in emails_with_words.keys():
                    emails_with_words[word] += 1
                else:
                    emails_with_words[word] = 1
        return emails_with_words

    def compare_words(self, spam_words: Dict[str, int], ham_words: Dict[str, int]):
        """
        finds the same words in spam and ham words
        and deletes everything else from those lists
        :param spam_words: dictionary of words as keys and number of their occurrence
        :param ham_words: dictionary of words as keys and number of their occurrence
        """
        other_words = []
        for spam_word in spam_words.keys():
            if spam_word not in ham_words.keys():
                other_words.append(spam_word)
        for word in other_words:
            del spam_words[word]
        other_words = []
        for ham_word in ham_words.keys():
            if ham_word not in spam_words.keys():
                other_words.append(ham_word)
        for word in other_words:
            del ham_words[word]

    def get_emails_with_tag(self, email_tag: str, truth: Dict[str, str], name_content_dict: Dict[str, str]) -> Dict[str, str]:
        """
        finds emails with the same tag (SPAM or OK)
        :param email_tag: SPAM/OK
        :param truth: dictionary of file name as a key and its tag(SPAM/OK) as a value
        :param name_content_dict: dictionary of file name as a key and its content as a value
        :return: dict_of_tag: dictionary of file name(only SPAM of only OK file) as a key
        and its content as a value
        """
        dict_of_tag = {}
        for fname, tag in truth.items():
            if tag == email_tag:
                dict_of_tag[fname] = name_content_dict[fname]
        return dict_of_tag

    def spams(self, truth: Dict[str, str], name_content_dict: Dict[str, str]) -> Dict[str, str]:
        """
        get dictionary of SPAM emails from TRAINING SET
        :param truth: dictionary of file name as a key and its tag(SPAM/OK) as a value
        :param name_content_dict: dictionary of file name as a key and its content as a value
        :return: dict_of_tag: dictionary of file name(only SPAM of only OK file) as a key
        and its content as a value
        """
        return self.get_emails_with_tag(SPAM_TAG, truth, name_content_dict)

    def hams(self, truth: Dict[str, str], name_content_dict: Dict[str, str]) -> Dict[str, str]:
        """
        get dictionary of OK emails from TRAINING SET
        :param truth: dictionary of file name as a key and its tag(SPAM/OK) as a value
        :param name_content_dict: dictionary of file name as a key and its content as a value
        :return: dict_of_tag: dictionary of file name(only SPAM of only OK file) as a key
        and its content as a value
        """
        return self.get_emails_with_tag(HAM_TAG, truth, name_content_dict)
