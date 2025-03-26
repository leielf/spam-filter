import os
from typing import List


class Corpus:
    def __init__(self):
        pass

    def emails(self, path: str):
        """
        goes through files and saves email name and its contents
        :param path: path to a file
        :return: dictionary of email name as a key
        and email content as a value
        """
        dictionary = {}
        all_fnames = os.listdir(path)
        fnames = []
        for name in all_fnames:
            if name[0] != '!':
                fnames.append(name)
        for fn in fnames:
            end = os.path.join('/', fn)
            fpath = path + end
            with open(fpath, encoding="utf-8") as f:
                content = ''
                for line in f.readlines():
                    line = line.strip()
                    content += (line + ' ')
                dictionary[fn] = content
        return dictionary

    def get_all_words(self, contents: List[str]):
        """
        creates a dictionary where keys are the words from all emails(spam or ham)
        and values are the number of times a particular word occurs in all emails
        :param contents: list of emails' contents
        :return: all_words: dictionary of a word as a key and number of its occurrence
        """
        all_words = {}
        for content in contents:
            content_words = self.get_words_from_email(content)
            for word, amount in content_words.items():
                if word in all_words.keys():
                    all_words[word] += amount
                else:
                    all_words[word] = amount
        return all_words

    def get_words_from_email(self, content):
        """
        get words only from 1 email
        :param content: list of contents of the email
        :return: valid_words: dictionary of a word as a key
        and number of its occurrence in an email as a value
        """
        signs = ['.', ',', '!', '?']
        content_words = content.split(' ')
        valid_words = {}
        for word in content_words:
            for sign in signs:
                while sign in word:
                    word = word.replace(sign, '')
            if word.isalpha():
                word = word.lower()
                if word in valid_words.keys():
                    valid_words[word] += 1
                else:
                    valid_words[word] = 1
        return valid_words



