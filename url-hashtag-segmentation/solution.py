# https://www.hackerrank.com/challenges/url-hashtag-segmentation

import sys

def clean_url(line0):
	i = 0
	line = line0[4:] if line0[0:4] == "www." else line0
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
	    words[words_lines[i].strip().lower()] = 0
	# print(words)
	return words

def is_number(num_str):
    try:
    	int(num_str)
    	return True
    except ValueError:
        try:
        	float(num_str)
        	return True
        except ValueError:
        	return False

def process_line(stack, line, words, current_word_start, j, consolidated):
	if j > len(line):
		if stack == []:
			return [(0, len(line))]
		else:
			(last_current_word_start, last_j, last_consolidated0) = stack.pop()
			last_consolidated = last_consolidated0.copy()
			last_consolidated.append((last_current_word_start, last_j))
			if last_j == len(line):
				return last_consolidated
			else: 
				return process_line(stack, line, words, last_j, last_j + 1, last_consolidated)
	else:
		current_word = line[current_word_start:j]
		if current_word in words:
			stack.append((current_word_start, j, consolidated))
		elif is_number(current_word):
			stack.append((current_word_start, j, consolidated))
		return process_line(stack, line, words, current_word_start, j + 1, consolidated)


            
def separate(lines, words):
	for line in lines:
		line_words = process_line([], line, words, 0, 1, [])
		line_words_print = []
		for (start, end) in line_words:
			line_words_print.append(line[start:end])
		print(" ".join(line_words_print))

if __name__ == '__main__':
	words = get_words()
	s = sys.stdin.read()
	lines = list(
    	filter(
			lambda x: x != " " and x != "",
			s.split("\n")))
	cleaned_lines = clean(lines[1:])
	# print(cleaned_lines)
	separate(cleaned_lines, words)
	# print(separated)

