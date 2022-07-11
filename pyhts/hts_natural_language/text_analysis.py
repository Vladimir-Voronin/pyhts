import re
from collections import Counter

from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


class TextAnalysis:
    def __init__(self):
        self.text = bytearray()

    @staticmethod
    def get_frequency_by_bytearray(source_b_array: bytearray) -> dict:
        pattern = r'[^A-z ]'
        text = source_b_array.lower().decode('utf-8')
        text = re.sub(pattern, '', text)

        words_list = text.split()  # tokenize function from nltk doesn't work correctly with "'" --> don't --> [do, n't]

        # stop-words filter
        stop_words = stopwords.words('English')
        text_w_stop_words = [word for word in words_list if word not in stop_words]

        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        lemm_list = [lemmatizer.lemmatize(word, 'v') for word in text_w_stop_words]
        frequency_dict = dict(Counter(lemm_list))

        return frequency_dict

    @staticmethod
    def get_frequency_by_list(words_list: list) -> dict:
        words_list = [word.strip() for word in words_list if word.strip() != ""]

        # stop-words filter
        stop_words = stopwords.words('English')
        text_w_stop_words = [word for word in words_list if word not in stop_words]

        # Lemmatize
        lemmatizer = WordNetLemmatizer()
        lemm_list = [lemmatizer.lemmatize(word, 'v') for word in text_w_stop_words]
        frequency_dict = dict(Counter(lemm_list))

        return frequency_dict
