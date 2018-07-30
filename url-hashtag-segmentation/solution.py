# https://www.hackerrank.com/challenges/url-hashtag-segmentation

import sys

def clean_url(line0):
	i = 0
	line = line0[4:] if line0[0] == 'w' else line0
	rline = list(reversed(line))
	last_dot = 0
	while i < len(line):
		if rline[i] == '.':
			if i > 0 and i < len(line) - 1:
				if rline[i - 1].isalpha():
					last_dot = i
			else:
				last_dot = i
		i+=1
	return line[0:len(line) - (last_dot+1)]


def clean(lines):
	return [
        	line[1:].strip().lower()
        if 
        	line[0] == '#' 
        else
        	clean_url(line).strip().lower()
        for line in lines 
    ]

def get_words():
	words_file = open("words.txt",'r')
	words_content = words_file.read()
	words_lines = list(
		filter(
			lambda x: x != " " and x != "",
			words_content.split("\n")))
	words = {}
	for i in range(0, len(words_lines)):
	    words[words_lines[i]] = 0
	# print(words)
	return words

def separate(lines, words):
	total_words = []
	for line in lines:
		terms = []
		j = 1
		current_word_start = 0
		last_ok = 0
		while j <= len(line):
			current_word = line[current_word_start:j]
			# print(current_word)
			if current_word in words:
				# print("IN WORDS")
				last_ok = j
			else:
				if last_ok != 0:
					terms.append(line[current_word_start:last_ok])
					current_word_start = j - 1
					last_ok = 0
					j-=1
			j+=1
		if last_ok != 0:
			terms.append(line[current_word_start:last_ok])
		if terms == [] or last_ok != len(line) :
			print(line)
			total_words.append([line])
		else :
			print(" ".join(terms))
			total_words.append(terms)
	return total_words
            

if __name__ == '__main__':
	words = get_words()
	s = sys.stdin.read()[1:]
	lines = list(
    	filter(
			lambda x: x != " " and x != "",
			s.split("\n")))
	cleaned_lines = clean(lines)
	# print(cleaned_lines)
	separated = separate(cleaned_lines, words)
	# print(separated)

