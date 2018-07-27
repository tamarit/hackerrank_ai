# https://www.hackerrank.com/challenges/the-trigram

import sys

def times_sublist_in_list(sublist, l):
    # print(sublist)
    # print(l)
    pos_sublist = 0
    total = 0
    for i in range(0, len(l)):
        # print(sublist[pos_sublist] + " " + l[i])
        if sublist[pos_sublist] == l[i]:
            # print(pos_sublist)
            pos_sublist += 1
            if pos_sublist == len(sublist):
                total += 1
                # print(total)
                pos_sublist = 0
        else:
            pos_sublist = 0
    return total 

     
def search_trigram(words):
    max_total = 0
    max_trigram = []
    for i in range(0, len(words)):
        for j in range(0, len(words[i]) - 2):# Only consdier items from the first till the one that is two places before the last
            trigram = words[i][j:j + 3]
            total = 1
            total += times_sublist_in_list(trigram, words[i][j + 3:])
            for k in range(i + 1, len(words)):
                total += times_sublist_in_list(trigram, words[k])
            # print(total)
            # print(max_total)
            # print(max_trigram)
            if total > max_total:
                # print(trigram)
                # print(total)
                max_total = total
                max_trigram = trigram
    return max_trigram
            

if __name__ == '__main__':
    s = sys.stdin.read()
    sentences = list(filter(lambda x: x != " ",s.split(".")))
    # print(sentences)
    words = []
    for i in range(0, len(sentences)):
        words.append(
            [
                x.lower().strip()  
                for x in sentences[i].split(" ") 
                if x != ''
            ])
        # words.append(
        #     list(map(
        #         lambda x: x.lower().strip(), 
        #         list(filter(
        #             lambda x: x != '', 
        #             sentences[i].split(" "))))))
    # print(words)
    print(" ".join(search_trigram(words)))




