"""
Write your reusable code here.
Main method stubs corresponding to each block is initialized here. Do not modify the signature of the functions already
created for you. But if necessary you can implement any number of additional functions that you might think useful to you
within this script.

Delete "Delete this block first" code stub after writing solutions to each function.

Write you code within the "WRITE YOUR CODE HERE vvvvvvvvvvvvvvvv" code stub. Variable created within this stub are just
for example to show what is expected to be returned. You CAN modify them according to your preference.
"""
import os
import re
import nltk


def block_reader(path):
    files = os.listdir(path)
    for file in files:
        if re.match('.+\\.sgm', file):
            reuters_file_content = open(path + '/' + file, 'r', encoding='iso8859').read()
            yield reuters_file_content


def block_document_segmenter(INPUT_STRUCTURE):
    regexp = re.compile('<REUTERS.*?</REUTERS>', re.S)
    for item in INPUT_STRUCTURE:
        document_text_list = regexp.findall(item)
        for document_text in document_text_list:
            yield document_text


def block_extractor(INPUT_STRUCTURE):
    id_regexp = re.compile('(?<=NEWID=\")\\d+(?=\")', re.S)
    text_regexp = re.compile('(?<=<BODY>).*(?=</BODY>)', re.S)

    for item in INPUT_STRUCTURE:
        news_id_list = id_regexp.findall(item)
        text_list = text_regexp.findall(item)
        new_id = news_id_list[0] if len(news_id_list) != 0 else ''
        text = text_list[0] if len(text_list) != 0 else ''
        content_dict = {"ID": new_id, "TEXT": text}
        if int(content_dict['ID']) <= 5:
            yield content_dict


def block_tokenizer(INPUT_STRUCTURE):
    for item in INPUT_STRUCTURE:
        text = item['TEXT']
        tokens = nltk.word_tokenize(text)
        for token in tokens:
            token_tuple = (item['ID'], token)
            yield token_tuple


def block_stemmer(INPUT_STRUCTURE):
    porter = nltk.PorterStemmer()
    for item in INPUT_STRUCTURE:
        token = porter.stem(item[1])
        token_tuple = (item[0], token)
        yield token_tuple


def block_stopwords_removal(INPUT_STRUCTURE, stopwords):
    def is_in_stopword_list(item):
        stopwords_list = stopwords.split("\n")
        if item[1] in stopwords_list:
            return False
        else:
            return True

    it = filter(is_in_stopword_list, INPUT_STRUCTURE)

    for item in tuple(it):
        yield item
