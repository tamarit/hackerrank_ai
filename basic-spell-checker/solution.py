import re
from collections import Counter
from string import ascii_lowercase

# import numpy as np

# def levenshtein(seq1, seq2):
#     size_x = len(seq1) + 1
#     size_y = len(seq2) + 1
#     matrix = np.zeros ((size_x, size_y))
#     for x in xrange(size_x):
#         matrix [x, 0] = x
#     for y in xrange(size_y):
#         matrix [0, y] = y

#     for x in xrange(1, size_x):
#         for y in xrange(1, size_y):
#             if seq1[x-1] == seq2[y-1]:
#                 matrix [x,y] = min(
#                     matrix[x-1, y] + 1,
#                     matrix[x-1, y-1],
#                     matrix[x, y-1] + 1
#                 )
#             else:
#                 matrix [x,y] = min(
#                     matrix[x-1,y] + 1,
#                     matrix[x-1,y-1] + 1,
#                     matrix[x,y-1] + 1
#                 )
#     print (matrix)
#     return (matrix[size_x - 1, size_y - 1])


def words(text):
    return re.findall(r'(?:[a-z]+[a-z\'\-]?[a-z]|[a-z]+)', text.lower())

def create_vocabulary():
    return Counter(words(open('corpus.txt').read()))

def mistake_1(w):
    returned = []
    for i in range(len(w)):
        returned.append(w[:i] + w[i+1:])
    return returned

def mistake_2(w):
    returned = []
    for i in range(len(w)):
        for c in ascii_lowercase:
            returned.append(w[:i] + c + w[i+1:])
    return returned

def mistake_3(w):
    returned = []
    for i in range(len(w) - 1):
        returned.append(w[:i] + w[i+1] + w[i] + w[i+2:])
    return returned

def mistake_4(w):
    returned = []
    for i in range(len(w) + 1):
        for c in ascii_lowercase:
            returned.append(w[:i] + c + w[i:])
    return returned

def mistakes(w):
    return mistake_1(w) + mistake_2(w) + mistake_3(w) + mistake_4(w)

def correct_words(ws, vocabulary):
    for w in ws:
        w = w.lower()
        if w in vocabulary:
            print(w)
            continue
        candidates = []
        for m in mistakes(w):
            if m in vocabulary:
                candidates.append((vocabulary[m], m))
        candidates = sorted(candidates, reverse=True)
        # print(candidates)
        if candidates == []:
            print(w)
            continue
        print(candidates[0][1])

if __name__ == "__main__":
    num_words = int(input().strip())
    ws = [input().strip() for i in range(num_words)]
    vocabulary = create_vocabulary()
    correct_words(ws, vocabulary)

