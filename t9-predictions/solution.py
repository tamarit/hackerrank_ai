# https://www.hackerrank.com/challenges/t9-predictions

import sys
import re
import string

def get_content(file_name):
    return open(file_name,'r').read()

def read_corpus():
    content = get_content("t9TextCorpus")
# A word is a sequence of characters (a-z, lowercase or uppercase; hyphen or apostrophe) 
# which always starts and ends with a letter (a-z, lowercase or uppercase). 
# The regex used must be greedy.
    p = re.compile(r"\b[a-z\-\']+\b", re.IGNORECASE)
    return p.findall(content)

def read_dictionary():
    content = get_content("t9Dictionary")
    lines = list(
        filter(
            lambda x: x != " " and x != "",
            content.split("\n")))[1:]
    dictionary = {}
    for line in lines:
        dictionary[line] = dictionary.get(line, 0) + 1
    return dictionary

def populate_dictionary(dictionary, corpus):
    for w in corpus:
        current_value = dictionary.get(w)
        if current_value != None:
            dictionary[w] = current_value + 1 

def get_t9_dict():
    # 2 abc
    # 3 def
    # 4 ghi
    # 5 jkl
    # 6 mno
    # 7 pqrs
    # 8 tuv
    # 9 wxyz
    all_chars = string.ascii_lowercase
    current_index = 0
    t9_dictionary = {}
    for j in range(2, 10):
        top = 4 if (j == 7 or  j == 9) else 3
        for i in range(current_index, current_index + top):
            t9_dictionary[all_chars[i]] = j  
        current_index += top
    return t9_dictionary

def translate_t9(words, t9_dict):
    result = map(
            lambda w: (w[0], w[1], "".join(map(
                lambda c: str(t9_dict.get(c, 0)), w[0]))),
            words)
    return list(result)

def predict(lines, t9_words):
    for l in lines:
        found = {}
        for (w, frec, t9str) in t9_words:
            index = t9str.find(l)
            if index == 0:
                current = found.pop(frec, [])
                current.append(w)
                found[frec] = current
            if len(found) == 5:
                break
        if len(found) == 0:
            print("No Suggestions")
        else:
            sorted_found = sorted(
                    found.items(), 
                    key=lambda x:x[0], 
                    reverse=True)
            # print(sorted_found)
            selected = []
            for (frec, list_words) in sorted_found:
                for word in sorted(list_words):
                    selected.append(word)
                    if len(selected) == 5:
                        break
                if len(selected) == 5:
                        break
            print(";".join(selected))

if __name__ == '__main__':
    s = sys.stdin.read()
    lines = list(
        filter(
            lambda x: x != " " and x != "",
            s.split("\n")))[1:]
    corpus = read_corpus()
    dictionary = read_dictionary()
    # print(corpus)
    # print(len(dictionary))
    # print(dictionary)
    populate_dictionary(dictionary, corpus)
    # table = str.maketrans('\'-abcdefghijklmnopqrstuvwxyz','}{zyxwvutsrqponmlkjihgfedcba')
    sorted_words = sorted(
        dictionary.items(), 
        key=lambda x:x[1], 
        reverse=True)
    # print(sorted_words)
    t9_dict = get_t9_dict()
    # print(t9_dict)
    t9_words = translate_t9(sorted_words, t9_dict)
    # print(t9_words)
    predict(lines, t9_words)









